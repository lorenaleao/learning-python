#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:03:02 2018
PROBLEM SET 1
PART A: HOUSE HUNTING
Determine how long it will take you to save enough 
money to make the down payment of my dream house

@author: lorenaleao
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))


portion_down_payment = 0.25 #the portion of the cost needed for a down payment 
current_savings = 0  #the amount that I have saved thus far
r = 0.04 #investing you current savings with an annual return of ​ r ​= 0.04 (4%). 

number_of_months = 0
while (current_savings < portion_down_payment*total_cost):
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    number_of_months += 1

print("Number of months:", number_of_months, "that is", number_of_months//12, "years and", number_of_months%12, "months.")