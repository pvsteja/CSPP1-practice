'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    inp_1 = ''
    line = int(input())
    for i in range(line):
        i += 1
        inp_1 = input()
        inp_1 += '\n'
    print(input)
if __name__ == '__main__':
    main()
