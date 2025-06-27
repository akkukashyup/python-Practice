# WAP to find the greatest of 3 numbers entered by the user.

A = int(input("enter the value :"))
B = int(input("enter the value :"))
C = int(input("enter the value :"))

if(A >= B and A >= C):
    print("first number is largest", A)
elif(B >= C):
    print("second number is largest", B)
else:
    print("third number is largest",C)        