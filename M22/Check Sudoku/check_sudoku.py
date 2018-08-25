'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):

    
def check_sudoku(lst_1):
    '''
    Your solution goes here. You may add other helper functions as needed.
    The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i in range(9):
        l = lst_1[i]
        if "".join(l.sort()) != "123456789":
            return False
    for i in range(9):
        for j in range(9):
            l.append(lst_1[j][i])
        if "".join(sorted(l)) != "123456789":
            return False
    
    if "".join(sorted(lst_1[0][0]+lst_1[0][1]+lst_1[0][2]+ lst_1[1][0]+ lst_1[1][1]+lst_1[1][2]+lst_1[2][0]+lst_1[2][1]+lst_1[2][2]))!= "123456789":
        return False
    if "".join(sorted(lst_1[0][3]+lst_1[0][4]+lst_1[0][5]+ lst_1[1][3]+ lst_1[1][4]+lst_1[1][5]+lst_1[2][3]+lst_1[2][4]+lst_1[2][5]))!= "123456789":
        return False  
    if "".join(sorted(lst_1[0][6]+lst_1[0][7]+lst_1[0][8]+ lst_1[1][6]+ lst_1[1][7]+lst_1[1][8]+lst_1[2][6]+lst_1[2][7]+lst_1[2][8]))!= "123456789":
        return False 
    if "".join(sorted(lst_1[3][0]+lst_1[3][1]+lst_1[3][2]+ lst_1[4][0]+ lst_1[4][1]+lst_1[4][2]+lst_1[5][0]+lst_1[5][1]+lst_1[5][2]))!= "123456789":
        return False
    if "".join(sorted(lst_1[3][3]+lst_1[3][4]+lst_1[3][5]+ lst_1[4][3]+ lst_1[4][4]+lst_1[4][5]+lst_1[5][3]+lst_1[5][4]+lst_1[5][5]))!= "123456789":
        return False
    if "".join(sorted(lst_1[3][6]+lst_1[3][7]+lst_1[3][8]+ lst_1[4][6]+ lst_1[4][7]+lst_1[4][8]+lst_1[5][6]+lst_1[5][7]+lst_1[5][8]))!= "123456789":
        return False
    if "".join(sorted(lst_1[6][0]+lst_1[6][1]+lst_1[6][2]+ lst_1[7][0]+ lst_1[7][1]+lst_1[7][2]+lst_1[8][0]+lst_1[8][1]+lst_1[8][2]))!= "123456789":
        return False
    if "".join(sorted(lst_1[6][3]+lst_1[6][4]+lst_1[6][5]+ lst_1[7][3]+ lst_1[7][4]+lst_1[7][5]+lst_1[8][3]+lst_1[8][4]+lst_1[8][5]))!= "123456789":
        return False
    if "".join(sorted(lst_1[6][6]+lst_1[6][7]+lst_1[6][8]+ lst_1[7][6]+ lst_1[7][7]+lst_1[7][8]+lst_1[8][6]+lst_1[8][7]+lst_1[8][8]))!= "123456789":
        return False
    return True

n = 9
lst_1 = []
for _ in range(n):
    lst_1.append(input().split())
print(check_sudoku(lst_1))

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        lst_1.append(input().split())
    # call solution function and print result to console
    print(check_sudoku(lst_1))

if __name__ == '__main__':
    main()