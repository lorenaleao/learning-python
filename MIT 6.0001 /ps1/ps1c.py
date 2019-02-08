#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:36:18 2019

@author: lorenaleao
"""
def calculate_savings(annual_salary, portion_saved_guess):
    current_savings = 0
    for i in range(1, number_of_months+1):
        current_savings += current_savings*r/12 + (portion_saved_guess/100)*annual_salary/12
        if(i % 6 == 0):
            annual_salary += annual_salary*semi_annual_raise
    return current_savings

annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000.0 #cost of your dream home: $1M
semi_annual_raise = .07 
portion_down_payment = 0.25 #the portion of the cost needed for a down payment 
current_savings = 0  #the amount that I have saved thus far
r = 0.04 #investing you current savings with an annual return of ​ r ​= 0.04 (4%). 

down_payment = portion_down_payment*total_cost
number_of_months = 36
low = 0
high = 10000
num_steps = 0

while (abs(current_savings - down_payment) > 100):
    num_steps += 1
    portion_saved_guess = (low+high)/2 #the percent of your salary to save
    current_savings = calculate_savings(annual_salary, portion_saved_guess)

    if current_savings < down_payment:
        low = portion_saved_guess
    else:
        high = portion_saved_guess
    
portion_saved = portion_saved_guess/100    
if portion_saved <= 1:
    print("Best savings rate: ", portion_saved_guess/100)
    print("Steps in bisection search: ", num_steps)
else:
    print("It is not possible to pay the down payment in three years.")
