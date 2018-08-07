"""Exercise: Assignment-2"""
# Write a Python function, sumofdigits
# that takes in one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.
def sumofdigits(n_m):
    '''
    n is positive Integer
        returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_m >= 1:
        return n_m%10 + sumofdigits(n_m//10)
    return 0
def main():
    """sumofdigits"""
    a_b = input()
    print(sumofdigits(int(a_b)))

if __name__ == "__main__":
    main()
