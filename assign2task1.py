
"""
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""
num1 = input("Enter a number : ")
if int(num1)%2 == 0:
    print(num1," is an even number")
else:
    print(num1," is an odd number")