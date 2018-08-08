"""Exercise: Is In"""
# Write a Python function, isIn(char, aStr)
# that takes in two arguments a character and String
# returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def is_in(char, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    len_str = len(a_str)
    if len_str == 0:
        return False
    else:
        if char == a_str[len_str//2]:
            return True
        elif char < a_str[len_str//2]:
            return is_in(char, a_str[:len_str//2])
        return is_in(char, a_str[len_str//2])

def main():
    """isinfunction"""
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
