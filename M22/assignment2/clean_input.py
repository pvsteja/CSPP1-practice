'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
"""clean string"""
def clean_string(str):
    for i in str:
        if i not in '!@#$%^&*()_+-=,.?1234567890':
            if i not in"'":
"""removing special characters"""
def main():
    str = input()
    print(clean_string(str))

if __name__ == '__main__':
    main()
    