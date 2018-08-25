'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

var_s = input()
var_x = 'bob'
count = 0
for i in range(len(var_s)):
    if var_x == var_s[i:i+3]:
        count = count + 1
print(count)

 