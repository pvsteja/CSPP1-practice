"""
defining the matrix multiplication and the matrix addition.
"""
def mult_matrix(1_mat, 2_mat):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(1_mat[0]) != len(2_mat):
        print("Error: Matrix shapes invalid for mult")
        return None
    # else:
    mul_result = []
    st_a = []
    # rows = len(1_mat)
    cols = len(2_mat[0])
    rows_2 = len(2_mat)
    for i, _ in enumerate(1_mat):
        # print(i, _)
        for j in range(cols):
            sum_value = 0
            for k in range(rows_2):
                sum_value += (1_mat[i][k] * 2_mat[k][j])
                k += 1
            st_a.append(sum_value)
            j += 1
        mul_result.append(st_a)
        i += 1
        st_a = []
    return mul_result

def add_matrix(1_mat, 2_mat):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(1_mat) != len(2_mat) and len(1_mat[0]) != len(2_mat[0]):
        print("Error: Matrix shapes invalid for addition")
        return None
    # else:
    add = []
    rows = len(1_mat)
    for i in range(rows):
        row = []
        for j in range(len(2_mat[0])):
            row.append(1_mat[i][j] + 2_mat[i][j])
            j += 1
        add.append(row)
        i += 1
    return add

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(',')
    rows = int(line[0])
    columns = int(line[1])
    matrix = []
    for _ in range(rows):
        line = input().split(" ")
        if len(line) == columns:
            matrix.append([int(j) for j in line])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    """
    calling the funtions and printing the output.
    """
    # read matrix 1
    1_mat = read_matrix()

    # read matrix 2
    2_mat = read_matrix()

    # print(1_mat)
    # print(2_mat)

    # add matrix 1 and matrix 2
    # matrix_sum = add_matrix(1_mat, 2_mat)
    if (1_mat and 2_mat):
        sum_matrix = add_matrix(1_mat, 2_mat)
        print(sum_matrix)
        print(mult_matrix(1_mat, 2_mat))
        # print(mult_mat)

    # multiply matrix 1 and matrix 2
    # matrix_mul = mult_matrix(1_mat, 2_mat)

if __name__ == '__main__':
    main()
