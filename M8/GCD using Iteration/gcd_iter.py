"""Exercise: GCDIter"""
# Write a Python function, gcd_iter(a_inp, b_inp), that takes in two numbers.
# returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
def gcd_iter(a_inp, b_inp):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    i = 1
    gcd_op = 1
    small_check = min(a_inp, b_inp)
    while i <= small_check:
        if a_inp%i == 0:
            if b_inp%i == 0:
                if i > 1:
                    gcd_op = i
        i += 1
    return gcd_op
def main():
    """gcd_iter"""
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
