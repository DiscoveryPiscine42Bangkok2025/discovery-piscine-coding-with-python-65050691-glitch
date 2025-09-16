num1 = int(input("Enter First Number"))
num2 = int(input("Enter the second number"))
if num1*num2 > 0:
        print(num1,"*",num2,"=",num1*num2)
        print("The result is positive")
elif num1*num2 < 0:
        print(num1,"*",num2,"=",num1*num2)
        print("The result is negative")
else:
       print(num1,"*",num2,"=",num1*num2) 
       print("The result is positive and negative")