'''
CIS 122 Spring 2016 Project1-2
Author: Arunima Bhattacharjee
Credit: Jonathan and lab help hours.
Description: Strings and Things, part 2
'''
# Problem (0)
sequence = input("Please enter some text: ")
result = ""
for letter in sequence:
    result = (result + letter*2)
print("Double string: ", result)
print()

# Problem (1)
a = input("Please enter some text: ")
b = (a[1:len(a)-1])
print("Letter reverse string: ",a[len(a)-1] + b + a[0]) 
print()

# problem (2)
a = input("Please enter name: ")
print("Hello,", a)
print()

# problem (3)
a = input("Please give dollar amount for stamps: ")
b = "First class stamps: "
print(b, int(int(a)//.49))
c = "Penny stamps: "
print(c, int(int(a)%.49))
print()

#Challenge - Oxford word challenge

#1
a = ("eat")
print(a[2] + a[0] + a[1])
print()

#2
b = ("brush")
print(b[3] + b[4] + b[1] + b[2] + b[0])
print()

#3
c = ("rail")
print(c[3] + c[2] + c[1] + c[0])
print()

#4
d = ("skate")
print(d[1] + d[4] + d[2] + d[3] + d[0])
print()

#5
e = ("wand")
print(e[3] + e[1] + e[0] + e[2])
print()

#6
f = ("alice")
print(f[3] + f[4] + f[1] + f[2] + f[0])
print()

#7
g = ("dorothea")
print(g[4] + g[5] + g[6] + g[1] + g[0] + g[3] + g[2] + g[7])
print()

#8
h = ("supersonic")
print(h[2] + h[3] + h[4]+ h[9] + h[1] + h[0] + h[5] + h[8] + h[6] + h[7])
print()

#9
i = ("hormone")
print(i[3] + i[4] + i[1] + i[2] + i[0] + i[6] + i[5])
print()

#10
j = ("spectrum")
print(j[3] + j[5] + j[6] + j[7] + j[1] + j[2] + j[4] + j[0])
print()

#11
k =("Which food might you make out of stale  lamb? ")
print(k + " meatballs")
print()

#12
j = ("What do you have to be if you want to listen? ")
print(j+ " silent")
