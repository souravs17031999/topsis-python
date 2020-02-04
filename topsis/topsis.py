"""
@ author : sourav kumar (101883068)
@ made for UCS633 - PROJECT - I
"""
import numpy as np
import pandas as pd
import re
import sys
# Class for topsis algorithm module
class topsis:
    # intializing following variables required for intermediate calculations
    """
    Attributes:
        matrix : numpy 2-D array consisting of all attributes values
        rows : count of rows in matrix
        columns : count of columns in matrix
        n_matrix : numpy 2-D array normalized matrix which is step1
        w_matrix : numpy 2-D array weighted normalized matrix which is step2
        weights : numpy column vector of input user weights
        impacts : numpy column vector of input impacts
        best : numpy column vector for all best values according to impact
        worst : numpy column vector for all worst values according to impact
        s_best : numpy row vector for all the norm calculated best values
        s_worst : numpy row vector for all the norm calculated worst values
        p_scores : numpy row vector consisting of all the scores calculated for each alternative
    """
    def __init__(self, file, weights, impacts):
        """
        Args:
            file : Name of csv file to be read
            weights : list of weights for each attribute
            impacts : list of true or false values whether impact is to be maximized or minimized
        """
        # check for proper csv file
        assert "csv" in f"{file}", "Could not recognize csv file, try checking your input file"
        df = pd.read_csv(file).iloc[:, 1:]
        # DATA PREPROCESSING
        # using regular expressions to extract only numeric values along with floating values
        for i in df:
            df[i] = [re.findall("[0-9]*\.[0-9]+|[0-9]+", str(x))[0] for x in df[i]]
        self.matrix = np.array(df, dtype = np.float64)
        # check for correct format of matrix
        assert len(self.matrix.shape) == 2, "Decision matrix a must be 2D"

        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        self.n_matrix = np.array([[0]*self.columns for _ in range(self.rows)], dtype = np.float64)
        self.w_matrix = np.array([[0]*self.columns for _ in range(self.rows)], dtype = np.float64)
        self.weights = np.array(weights, dtype = np.float64)
        # check for correct format of weights
        assert len(self.weights.shape) == 1, "Weights array must be 1D"
        assert self.weights.size == self.columns, f"Weights array wrong length, should be of length {self.columns}"

        self.impacts = np.array(impacts)
        # check for correct format of impacts
        assert len(self.impacts.shape) == 1, "Impact array must be 1D"
        assert self.impacts.size == self.columns, f"Impacts array wrong length, should be of length {self.columns}"

        self.best = np.array([0]*self.columns, dtype = np.float64)
        self.worst = np.array([0]*self.columns, dtype = np.float64)
        self.s_best = np.array([0]*self.rows, dtype = np.float64)
        self.s_worst = np.array([0]*self.rows, dtype = np.float64)
        self.p_scores = np.array([0]*self.rows, dtype = np.float64)

    # step for calculation of normalized matrix using norm method
    def normalized_matrix(self):
        for i in range(self.columns):
            temp = np.sum(self.matrix[:, i]**2)**0.5
            self.n_matrix[:, i] = self.matrix[:, i] / temp

    # step for calculation of weighted normalized matrix
    def weighted_matrix(self):
        for i in range(self.columns):
            self.w_matrix[:, i] = self.n_matrix[:, i] * self.weights[i]

    # step for calculating best and worst values for all attributes
    def ideal_calculate(self):
        for i in range(self.columns):
            if self.impacts[i] == '+':
                self.best[i] = np.max(self.w_matrix[:, i])
                self.worst[i] = np.min(self.w_matrix[:, i])
            else:
                self.best[i] = np.min(self.w_matrix[:, i])
                self.worst[i] = np.max(self.w_matrix[:, i])

    # step for calculating p_scores which are calculated using euclidean distance norm and
    # calculate all the ranks using argsort
    def rank_calculate(self):
        for i in range(self.rows):
            self.s_best[i] = np.sum((self.w_matrix[i, :] - self.best)**2)**0.5
            self.s_worst[i] = np.sum((self.w_matrix[i, :] - self.worst)**2)**0.5
        self.p_scores = self.s_worst/(self.s_best + self.s_worst)
        final_scores_sorted = np.argsort(self.p_scores) # this returns indices of elements in sorted order
        max_index = len(final_scores_sorted)
        # printing final results
        print("Models   Rank")
        for i in range(len(final_scores_sorted)):
            print(f"M{i + 1}      {max_index - np.where(final_scores_sorted==i)[0]}") # since we know final_scores_sorted is already sorted, so
            # it i need ranking from back side, so we need to subtract from maximum and get first value of tuple returned by np.where function
        print(f"Result : Model/Alternative {np.argsort(self.p_scores)[-1] + 1} is best")

    # displaying all the intermediate matrices calculations
    def display(self):
        print('DISPLAYING ALL INNER MATRICES FOR MORE INFORMATION:')
        print('Original Matrix :')
        print(self.matrix)
        print('Nomralized Matrix : ')
        print(self.n_matrix)
        print('Weighted Matrix : ')
        print(self.w_matrix)
        print('Best values : ')
        print(self.best)
        print('Worst Values : ')
        print(self.worst)
        print('S_best Values : ')
        print(self.s_best)
        print('S_worst Values : ')
        print(self.s_worst)
        print('Performace Scores : ')
        print(self.p_scores)

    # main topsis functions caller to execute all the steps of the algorithm
    def topsis_main(self, debug = False):
        self.normalized_matrix()
        self.weighted_matrix()
        self.ideal_calculate()
        print()
        self.rank_calculate()
        if debug:
            print()
            self.display()
# main driver function
if __name__ == '__main__':
    print('WELCOME TO TOPSIS RANKING ALGORITHM')
    print('EXPECTED ARGUMENTS TO BE IN ORDER : python -m topsis.topsis <InputDataFile> <Weights> <Impacts> <Verbose(optional)>')
    if len(sys.argv) >= 4:
        file = sys.argv[1]
        weights = list(map(float, sys.argv[2].strip().split(',')))
        impacts = list(sys.argv[3].strip().split(','))
        print(f"Given csv file : {file} ")
        print(f"Given weights : {weights}")
        print(f"Given impacts : {impacts}")
        t = topsis(file, weights, impacts)
        if len(sys.argv) == 5:
            print()
            t.topsis_main(debug = True)
        else:
            t.topsis_main()
    else:
        print("PUT ARGUMENTS IN ORDER : python -m topsis.topsis <InputDataFile> <Weights> <Impacts> <Verbose>(optional)>")

    # if want to use argparser constraining on some flags
    # parser = argparse.ArgumentParser(description='Topsis algorithm')
    # parser.add_argument("-f", help="input csv file name",type=str)
    # parser.add_argument("-w", help="input weights",type=str)
    # parser.add_argument("-i", help="input impacts using + or -",type=str)
    # parser.add_argument("-v", help="enter any number to display output matrices otherwise only final result will be shown",type=int)
    # args = parser.parse_args()
    # file = args.f
    # weights = list(map(float, args.w.split(',')))
    # impacts = list(args.i.split(','))
    # print(file)
    # print(weights)
    # print(impacts)
