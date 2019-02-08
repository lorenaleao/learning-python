#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:55:17 2018
PROBLEM SET 1
PART B: SAVING, WITH A RAISE
Determine how long it will take you to save enough 
money to make the down payment of my dream house
assuming that your salary will increase every six months

@author: lorenaleao
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:​ "))


portion_down_payment = 0.25 #the portion of the cost needed for a down payment 
current_savings = 0  #the amount that I have saved thus far
r = 0.04 #investing you current savings with an annual return of ​ r ​= 0.04 (4%). 

number_of_months = 0
while (current_savings < portion_down_payment*total_cost):
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    number_of_months += 1
    if(number_of_months % 6 == 0):
        annual_salary += annual_salary*semi_annual_raise
        

print("Number of months:", number_of_months, "that is", number_of_months//12, "years and", number_of_months%12, "months.")
