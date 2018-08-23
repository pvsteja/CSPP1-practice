def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mult_matrix = []
    a = []
    b = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                sum = 0
                for k in range(len(m2)):
                    sum = sum + (m1[i][k]*m2[k][j])
                    k += 1
                a.append(sum)
                j += 1
            b.append(a)
            i += 1
            a = []
        return b
    print("Error: Matrix shapes invalid for mult")
    return None

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_matrix = []
    if len(matrix_1) == len(matrix_2):
        for i in range(len(matrix_1)):
            lst = []
            for j in range(len(matrix_1[0])):
                lst.append(int(matrix_1[i][j]) + int(matrix_2[i][j]))
                j += 1
            add_matrix.append(lst)
            i += 1
        return add_matrix
    print("Error: Matrix shapes invalid for addition")
    return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(",")
    rows = int(line[0])
    cols = int(line[1])
    matrix = []
    for i in range(rows):
        line = input().split(" ")
        if len(line) == cols:
        # print(i, line)
        # lst = []
        # for j in line:
        #     lst.append(int(j))
        # matrix.append(lst)
            matrix.append([int(j) for j in line])
            i += 1
        print("Error: Invalid input for the matrix")
        return None
    # print(rows, cols)
    # print(matrix)
    return matrix

def main():
    # read matrix 1
    matrix_1 = read_matrix()

    # read matrix 2
    matrix_2 = read_matrix()

    # add matrix 1 and matrix 2
    if matrix_1 != None and matrix_2 != None:
        print(add_matrix(matrix_1, matrix_2))
        print(mult_matrix(matrix_1, matrix_2))

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
