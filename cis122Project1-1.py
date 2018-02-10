'''
CIS 122 Spring 2016 Project1-1
Author: Arunima Bhattacharjee
Credit: Jonathan and lab help hours.
Description: Strings and Things, part 1
'''
#(0)Tip Calculator
total_amount_bill = input("please enter total bill")
print("suggested tip for 15% ",float(total_amount_bill)*.15)
print("suggested tip for 18% ", round(float(total_amount_bill)*.18,2))
print("suggested tip for 20% ", float(total_amount_bill)*.20)
print()

#(1)Fancy Name Display
Name = input("please enter your name: ")
print((len(Name)+6)*"*")
print("*  "+Name+"  *")
print((len(Name)+6)*"*")
print()

#(2) Monogram-R-US
first = input("Please enter your first name: ")
print (first)
second = input ("Please enter your middle initial: ")
print(second)
third = input ("Please enter your last name: ")
print(third)
print(first[0:1]+ second[0:1] + third [0:1])

print()

#(3)Double-len
a = input("Please input string to check: ")
print(a)
b = "Length of input string: "
print(b ,(len(a)))
c = "Python length for input string: "
count = 0
for char in a: 
    count += 1
print(c, count)
