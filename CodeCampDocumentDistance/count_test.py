def check(input1):
    test = "test.txt"

    test1 = "test1.txt"
    test2 = "test2.txt"
    list_1 = ''
    count = 0
    count_c = 0
    count_d = 0
    for i in input1:
        if i not in "!@#$%^&*()_+-=,.?1234567890\'":
            list_1 += i
    # print(list_1) 
    list_1 = list_1.lower().split()
    for i in list_1:
        if i in load_stopwords(test)[0]:
            # print("abcd")
            count += 1
        if i in load_stopwords(test1)[0]:
            # print('def')
            count_c += 1
        if i in load_stopwords(test2)[0]:
            # print('efg')
            count_d += 1
    # print(count_c)
    # print(count_d)
    # print(count)
    return (count, count_c, count_d)
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = []
    with open(filename, 'r') as file:
        for line in file:
            stopwords.append(line.split())
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    print(check(input1))
if __name__ == '__main__':
    main()
