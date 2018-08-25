import re
"""clean special characters"""
def clean_string(string):
    input_1 = ' '
    reg = re.compile(["a-z, 0-9, A-Z"])
    input_1 = re.sub("", string.strip())
    return input_1
"""removing special characters"""
def main():
    string = input()
    print(clean_string(string.replace(" ","")))
if __name__ == '__main__':
    main()
    