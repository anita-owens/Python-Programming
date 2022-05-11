#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 08:30:05 2018

@author: anitaowens




"""

"""Week 1 Practice Exercises for Expressions
Solve each of the practice exercises below. Each problem includes two
 CodeSkulptor3 links: one for a template that you should use as a starting point for your solution and one
 to our solution to the exercise. (Note that these exercises may take longer than 10 minutes as indicated on
 Coursera's course content page.)

Note that many of these exercises focus on converting a mathematical formula in an equivalent Python expression.
For these exercises, we will always provide the formula. Your task is to write the Python expression.

1. There are  feet in a mile. Write a Python statement that calculates and prints the number
 of feet in  miles. Miles to feet template --- Miles to feet solution
 
 
2. Write a Python statement that calculates and prints the number of seconds in  hours, minutes and
  seconds. Hours to seconds template --- Hours to seconds solution
  
  
3. The perimeter of a rectangle is , where  and  are the lengths of its sides. 
Write a Python statement that calculates and prints the length in inches of the perimeter of a rectangle with
 sides of length  and  inches. Perimeter of rectangle template ---Perimeter of rectangle solution
 
 
4. The area of a rectangle is , where  and  are the lengths of its sides. Note that the multiplication operation is not shown explicitly in this formula. This is standard practice in mathematics, but not in programming. Write a Python statement that calculates and prints the area in square inches of a rectangle with sides of length  and  inches. Area of rectangle template --- Area of rectangle solution
The circumference of a circle is  where  is the radius of the circle. Write a Python statement that calculates and prints the circumference in inches of a circle whose radius is inches. Assume that the constant . Circumference of circle template --- Circumference of circle solution
The area of a circle is  where  is the radius of the circle. (The raised  in the formula is an exponent.) Write a Python statement that calculates and prints the area in square inches of a circle whose radius is  inches. Assume that the constant . Area of circle template --- Area of circle solution
Given  dollars, the future value of this money when compounded yearly at a rate of percent interest for  years is . (Remember that you don't need to understand how this formula works, only how to translate it into Python.) Write a Python statement that calculates and prints the value of  dollars compounded at  percent interest for years. Future value template --- Future value solution
Write a single Python statement that combines the three strings , and  (plus a couple of other small strings) into one larger string  and prints the result. (Hint: Experiment with adding two strings in Python using the  operator.) Name tag template --- Name tag solution
Write a Python expression that creates the string from several strings including  and the number  and then prints the result (Hint: Use the function  to convert the number into a string.) Name and age template --- Name and age solution
Challenge: The distance between two points  and  is . Write a Python statement that calculates and prints the distance between the points  and . (Hint: Remember that a square root can be computed by raising a value to the  power.) Point distance template --- Point distance solution

"""

"""use command plus I to run code"""

print("Hello World!")

message = "Hello Python World!"
print(message)
message = "Hello Python Crash Course World!"
print(message)

name="ada lovelace"
print(name.title())
print(name.upper())

first_name = "ada"
last_name = "lovelace"

full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("Python!")
print("\tPython!")

print("Languages:\nPython\nC\nJava")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language='python '
favorite_language.rstrip()
favorite_language



def myfunction(number):
    if number > 100
        return True
    return False
    
    myfunction(99)
