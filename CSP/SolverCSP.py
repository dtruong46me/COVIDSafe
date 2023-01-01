import random
import time
from ortools.sat.python import cp_model

class CSPSolution(cp_model.CpSolverSolutionCallback):
    def __init__(self,variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.Array = []

    def on_solution_callback(self):
        lines = []
        for v in self.__variables:
            lines.append(self.Value(v))
        self.Array.append(lines)

class Solver:
    def __init__(self,path_to_board: str = None, path_to_command: str = None):
        if path_to_board == None:
            path_to_board = 'board.out'
        self.board_path = path_to_board
        
        if path_to_command == None:
            path_to_command = 'command.inp'
        self.command_path = path_to_command

        self.__iter = 1
        self.solved = False
        self.__finished = False
        self.__undiscoverd = []
        self.csp_variables = []
    
    def __read_board(self):
        path = self.board_path
        self.__undiscoverd = []
        while True:
            with open(path,mode = 'r') as board:
                try:
                    iter = int(board.readline())
                    if iter < self.__iter:
                        self.__iter = iter + 1
                        lines = board.readlines()
                        board_state = []

                        for row_idx,line in enumerate(lines):
                            line = line.replace('\n','') 
                            cells_list = line.split(',')
                            board_state.append(cells_list)
                        
                            for col_idx,cell in enumerate(lines):
                                if cell == ' ':
                                    self.__undiscoverd.append(row_idx,col_idx)
                        
                        self.__board_state = board_state
                        return
                except ValueError:
                    pass

    def __write_command(self):
        with open(self.command_path,mode = 'w') as cmd:
            cmd.write(f'{self.__iter}\n')
            self.__iter += 1
            cmd.close()

    def __csp_model(self,board_size: int):
        model = cp_model.CpModel()
        A = [[' ' for i in range(board_size)] for j in range(board_size)]
        x = [[0 for i in range(board_size)] for j in range(board_size)]

        # SetVariables
        for row in range(board_size):
            for col in range(board_size):
                if A[row][col] == ' ':
                    continue
                
                if col < board_size-1 and A[row][col+1] == ' ':
                    x[row][col+1] = model.NewIntVar(0,1,'x[{}][{}]'.format(row,col+1))
                
                if row < board_size-1 and A[row+1][col] == ' ':
                    x[row+1][col] = model.NewIntVar(0,1,'x[{}][{}]'.format(row+1,col))

                if row > 0 and A[row-1][col] == ' ':
                    x[row-1][col] = model.NewIntVar(0,1,'x[{}][{}]'.format(row-1,col))

                if col > 0 and A[row][col-1] == ' ':
                    x[row][col-1] = model.NewIntVar(0,1,'x[{}][{}]'.format(row,col-1))

                if row < board_size-1 and col < board_size-1 and A[row+1][col+1] == ' ':
                    x[row+1][col+1] = model.NewIntVar(0,1,'x[{}][{}]'.format(row+1,col+1))

                if row > 0 and col > 0 and A[row-1][col-1] == ' ':
                    x[row-1][col-1] = model.NewIntVar(0,1,'x[{}][{}]'.format(row-1,col-1)) 

                if row > 0 and col < board_size-1 and A[row-1][col+1] == ' ':
                    x[row-1][col+1] = model.NewIntVar(0,1,'x[{}][{}]'.format(row-1,col+1)) 

                if row < board_size-1 and col > 0 and A[row+1][col-1] == ' ':
                    x[row+1][col-1] = model.NewIntVar(0,1,'x[{}][{}]'.format(row+1,col-1)) 

        # SetConstraints
        for row in range(board_size):
            for col in range(board_size):
                if A[row][col] == ' ' or A[row][col] == 0 or A[row][col] == 'X':
                    continue

                if row > 0 and row < board_size-1 and col > 0 and col < board_size-1:
                    model.Add(x[row-1][col-1]+x[row-1][col]+x[row-1][col+1]+\
                        x[row][col-1]+x[row][col+1]+x[row+1][col-1]+x[row+1][col]+\
                            x[row+1][col+1] == A[row][col])

                if row == 0 and col > 0 and col < board_size-1:
                    model.Add(x[row][col-1]+x[row][col+1]+x[row+1][col-1]+x[row+1][col]+\
                        x[row+1][col+1] == A[row][col])

                if col == 0 and col > 0 and col < board_size-1:
                    model.Add(x[row-1][col]+x[row-1][col+1]+x[row][col+1]+x[row+1][col]+\
                        x[row+1][col+1] == A[row][col])
            
                if row == board_size-1 and col > 0 and col < board_size-1:
                    model.Add(x[row-1][col-1]+x[row-1][col]+x[row-1][col+1]+x[row][col-1]+\
                        x[row][col+1] == A[row][col])

                if col == board_size-1 and row > 0 and row < board_size-1:
                    model.Add(x[row-1][col-1]+x[row-1][col]+x[row][col-1]+x[row+1][col-1]+\
                        x[row+1][col] == A[row][col])

                if row == 0 and col == 0:
                    model.Add(x[row][col+1]+x[row+1][col]+x[row+1][col+1] == A[row][col])

                if row == 0 and col == board_size-1:
                    model.Add(x[row][col-1]+x[row+1][col-1],x[row+1][col] == A[row][col])
                
                if row == board_size-1 and col == 0:
                    model.Add(x[row-1][col],x[row-1][col+1],x[row][col+1] == A[row][col])
                
                if row == board_size-1 and col == board_size-1:
                    model.Add(x[row-1][col-1]+x[row-1][col]+x[row-1][col] == A[row][col])

        # Creat Solver
        for row in range(board_size):
            for col in range(board_size):
                if type(x[row][col]) != int:
                    self.csp_variables.append(x[row][col])

        csp_solver = cp_model.CpSolver()
        csp_solution = CSPSolution(self.csp_variables)
        csp_solver.parameters.enumerate_all_solutions = True
        status = csp_solver.Solve(model,csp_solution)

        return csp_solution.Array

    def check_solution(self):
        cp_sol = self.__csp_model()
        if len(cp_sol) == 0:
            return
        if len(cp_sol) == 1:
            return cp_sol
        else:
            pass
        return

    def update(self):
        return

    def __check_finished(self):
        has_V = False
        for row in self.__board_state:
            if 'V' in row:
                has_V = True
                self.__finish = True
            if ' ' in row:
                if has_V:
                    self.solved = False
                    return
        if has_V:
            self.solved = True

    def Solve(self):
        self.__iter = 1
        while True:
            self.__read_board()
            self.__check_finished()
            self.__csp_model()
            if self.__finished:
                break

            self.__write_command() # Randomly
        
        