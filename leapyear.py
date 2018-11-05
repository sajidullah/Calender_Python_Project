# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:08:32 2018

@author: sajid Ullah
"""

# Python program to check if the input year is a leap year or not

#year = 2000
age = input("Enter the year:")
# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))