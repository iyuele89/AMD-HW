import math
import os
import random
import re
import sys
import calendar

# Say "Hello, World!" With Python

print("Hello, World!")

# Hello, World.

input_string = input()
print('Hello, World.')
print(input_string)


# Data Types

i_1 = 0 
d_1 = 0.0
s_1 = ""
i_1 = int(input()) 
d_1 = float(input())
s_1 = str(input())
print(i + i_1)
print(d + d_1)
print(s + s_1)


#Python If-Else

n = int(input())
if n % 2 == 0:
    if n in range(2,6):
        print("Not Weird")

    elif n in range(6,21):
        print("Weird")

    elif n > 20:
        print("Not Weird")
else:
    print("Weird")


#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops

if __name__ == '__main__':
    n = int(input())
    counter = 0
    while counter < n:
        print(counter ** 2)
        counter+=1



# Operators

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100   
    totalCost = round(meal_cost + tip + tax)
    return(totalCost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
    
    
# Intro to Conditional Statements

if __name__ == '__main__':
    N = int(input())
    print("Weird" if ((N%2!=0) or (N%2==0 and N in range(6,21))) else "Not Weird")
    

#Class vs. Instance

class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        if self.age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        
    def amIOld(self):
        if self.age < 13:
            print("You are young.")  
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")   
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1
        
        
# Print Function


if __name__ == '__main__':
    n = int(input())
    for n_1 in range(1, n+1):
        print(n_1, end="")
        
    
# Write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:  
            leap = True        
                        
    return leap
    

# List Comprehensions


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

cuboid = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i +j + k) != n]
print(cuboid)
        
        
        
# Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])
    

# Loops

if __name__ == '__main__':
    n = int(raw_input())
for i in range(1, 11):
    print("{} x {} = {}".format(n, i, n*i))
        
 
# Let's Review

for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])
    
# Arrays

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    for i in range(n):
        print(arr[i], end=" ")
        
 # Nested Lists

 
 if __name__ == '__main__':
    a = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])
a.sort()
a_1 = [i for i in a if i[0] != a[0][0]]
a_2 = [j for j in a_1 if j[0] == a_1[0][0]]
for k in range(len(a_2)):
    print(a_2[k][1])
        
     
# Finding the percentage


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a = student_marks[query_name]
    a_1 = sum(a)/3
    print('%.2f' % (a_1))
        
    
    
# Lists

L = []
for _ in range(int(input())):
    command, *args = input().split()
    try:
        getattr(L, command)(*(int(x) for x in args))
    except AttributeError:
        print(L)
        
        
 
# Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
       
   
# Exceptions

for i in range(int(input())):   
    try: 
        a,b=map(int,input().split())     
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
        
        
# Map and Lambda Function


 cube = lambda x: pow(x, 3)

def fibonacci(n):
    arr = [0, 1]
    for j in range(n-2):
        arr.append(arr[j] + arr[j+1])
    return arr[:n]
        
  
# Calendar Module

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())

        
        
        
        
        
        
        
        
        
        
 
