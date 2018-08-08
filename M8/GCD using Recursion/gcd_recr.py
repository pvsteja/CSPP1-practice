"""Exercise: GCDRecr"""
# Write a Python function, gcdRecur(a, b), that takes in two numbers.
# returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
def gcd_recur(a_inp, b_inp):
    '''
    a_inp, b_inp: positive integers
    returns: a positive integer, the greatest common divisor of a_inp & b_inp.
    '''
    # Your code here
    if b_inp == 0:
        return a_inp
    #else:
    return gcd_recur(b_inp, a_inp%b_inp)
def main():
    """gcd_recur"""
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
