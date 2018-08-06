
def main():
    """to print a string with out vowels"""
var_a = "hello world"
var_b = ""
for char in var_a:
    if char in "a,e,i,o,u":
        var_b = var_b + "*"
    else:
        var_b = var_b + char
print(var_b)
if __name__ == "__main__":
    main()
 