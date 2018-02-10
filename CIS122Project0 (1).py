'''
CIS 122 Spring 2016 Problem 0
Author: Arunima Bhattacharjee
Credit: Mostly worked by myself but I also got help at the lab help hours.
Description: Introduction to programming problem set uses Python numeric data types operations to solve a variety of small problem
'''
ttl_shirts = 15
ttl_green = 4
ttl_yellow = 11
cost_green = 25
cost_yellow = 15
ttl_cost = (ttl_green* cost_green ) + ( ttl_yellow*cost_yellow)
print(ttl_cost)
#If the print(ttl_cost) line of code is not included in the python file then it will not show on the shell, it will calculate it but it won't show to the user
print() 

#problem1
pi = 3.14159
Radius1 = 1
Radius2 = 5
Volume_sphere1 = (4/3)*(pi)*(Radius1**3)
Volume_sphere2 = (4/3)*(pi)*(Radius2**3)
print(Volume_sphere1)
print(Volume_sphere2)

#problem2
#In 1 day there are (24*60)= 1440 minutes
Day1 = 1440
Day365 = Day1 * 365
print (Day365)
print ("The number in the song is correct") 

#problem3
#Assuming there are 30 days
Day0= 0.01
Day1= Day0*2
Day30 = Day0*(2**30)
print (Day30)
print ("I choose 1 cent and double it each day of the month") 

#If it were 10 million, I would still stick with 1 cent a day and double it for each day of the month.
