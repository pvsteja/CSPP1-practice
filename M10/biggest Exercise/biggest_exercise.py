#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(a_Dict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    i = 0
    L = []
    if len(a_Dict) == 0:
        return 0
    print(a_Dict)
    for k in a_Dict:
        if len(a_Dict[k]) >= i:
            i = len(a_Dict[k])
            L=k
    return str(L)
def main():
    n=input()
    a_Dict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in a_Dict:
            a_Dict[l[0][0]]=[l[1]]
        else:
            a_Dict[l[0][0]].append(l[1])
    print(biggest(a_Dict))


if __name__== "__main__":
    main()