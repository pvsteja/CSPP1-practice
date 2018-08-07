"""Exercise: powerIter"""
# Write a Python function, iter_power(base, exp),
# that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    count = 1
    while exp != 0:
        count = count*base
        exp -= 1
    return count

def main():
    """power_iteration"""
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
