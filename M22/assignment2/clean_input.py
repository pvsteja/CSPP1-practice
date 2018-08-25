'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
"""clean string"""
import re
def clean_string(string):
    inp_1 = ' '
    reg = re.compile(["a-z, 0-9, A-Z"])
    inp_1 = re.sub("", string.strip())
    return inp_1
"""removing special characters"""
def main():
    string_1 = input()
    print(clean_string(string_1.replace(" ","")))
if __name__ == '__main__':
    main()
    