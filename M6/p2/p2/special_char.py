'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    var_a = input("")
    var_b = ""
    for char in var_a:
        if char in "!@#$%^&*":
            var_b = var_b +" "
        else:
            var_b = var_b + char
    print(var_b)
if __name__ == "__main__":
    main()
