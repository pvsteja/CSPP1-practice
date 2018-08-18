""" # given input product the individual number example 123 output should be  6"""
I_NT = int(input())
I_C = 1
C_O = 1
NU_M = 1
if I_NT < 0:
    NU_M = -1
    I_NT = abs(I_NT)
else:
    NU_M = 1
if I_NT != 0:
    while I_NT >= 1:
        C_O = I_NT % 10
        I_C = I_C*C_O
        I_NT = I_NT // 10
    print(NU_M*I_C)
else:
    print("0")
