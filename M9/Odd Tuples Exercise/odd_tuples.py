"""Exercise : Odd Tuples"""
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input.
#returns a tuple in which contains odd index values in the input tuple.
def odd_tuples(a_tup):
    '''
    a_tup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    n_w = len(a_tup)
    new_tuple = ()
    i = 0
    for i in range(n_w):
        if i%2 != 0:
            new_tuple = new_tuple + (a_tup[i],)

    return new_tuple
def main():
    """odd_tuples"""
    data = input()
    data = data.split()
    a_tup = ()
    for j in enumerate(data):
        a_tup += (data[j],)
    print(odd_tuples(a_tup))
main()
