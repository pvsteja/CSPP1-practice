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
    if len(M_1) == len(M_2):
        for i in range(M_1):
            for j in range(M_2[0]):
                sum = 0
                for k in range(len(M_2)):
                    sum = sum + (m1[i][k]*m2[k][j])
                a.append(sum)
            b.append(a)
            a = []
        return b

def add_matrix(M_1, M_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_matrix = []
    if len(M_1) == len(M_2):
        for i in range(len(M_1)):
            lst =[]
            for j in range(len(M_1[0])):
                lst.append(int(M_1[i][j]) + int(M_2[i][j]))
            add_matrix.append(lst)
        return add_matrix
    else:
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
        else:
            print("Error: Invalid input for the matrix")
            return None
    # print(rows, cols)
    # print(matrix)
    return matrix
      

def main():
    # read matrix 1
    M_1 = read_matrix()

    # read matrix 2
    M_2 = read_matrix()

    # add matrix 1 and matrix 2
    if M_1 != None and M_2 != None:
        print(add_matrix(M_1,M_2))
        print(mult_matrix(M_1, M_2))

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
