"""Exercise: Assignment-1"""
# Write a Python function, factorial(n)
# that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number.
def fact(n_m):
    '''
    n_m is positive Integer

    returns: a_b positive integer, the factorial of n.
    '''
    # Your code here

    if n_m <= 1:
        return 1
    return n_m*fact(n_m-1)
def main():
    """assignment1fact"""
    a_b = input()
    print(fact(int(a_b)))

if __name__ == "__main__":
    main()
