# -*- coding: utf-8 -*-

import argparse
import sys
import numpy as np
import pandas as pd

def read(args):
    Array = pd.read_table(str(args.pch_file),delim_whitespace=True,skiprows=4, names=['A','B','C','D'])

    Result=np.zeros((6, 6))

    BLOCK = False
    for index, row in Array.iterrows():
    #    print('%s \t %s \t %s \t %s' % (row['A'],row['B'],row['C'],row['D']))
        if row['A'] == 'DMIG*':
            if BLOCK == False:
                ResultRow = row['D']
            
            BLOCK = True

        elif row['A'] == '$':
            BLOCK = False

        if row['A'] == '*':
            Result[int(ResultRow)-1][int(row['C'])-1] = float(row['D'].replace('D','E'))
            
    Nodes = list(set(Array['B'].tolist()))
    np.set_printoptions(precision=2)
    Complete_Result = Result-np.triu(Result.T,)+Result.T


    print(' ')
    print('Stiffness matrix: %s' % (str(args.pch_file)))
    print(' ')
    print(Complete_Result)


    
def main():

    '''Console script'''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_foo1 = subparsers.add_parser('read')
    # An argument without - is required
    parser_foo1.add_argument('pch_file', type=str, help='PCH file to read')
    parser_foo1.set_defaults(func=read)


    if len(sys.argv) <=1:
        sys.argv.append('--help')

    # Show help if no arguments are given
    args = parser.parse_args()
    args.func(args)
    
    
if __name__ == "__main__":
    main()
