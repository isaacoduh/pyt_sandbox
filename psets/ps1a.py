'''
    Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. 

    Your program should ask the user to enter the following variables:
    1. The starting annual salary (annual_salary)
    2. The portion of salary to be saved (portion_saved)
    3. The cost of your dream home (total_cost)

'''

annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter portion of salary to be saved: '))
total_cost = float(input('Enter the cost of your dream_home: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

months = 0
monthly_salary = annual_salary / 12

cost_down_payment = total_cost * portion_down_payment

while current_savings <= cost_down_payment:
    current_savings = current_savings + ( current_savings * r/12) + (portion_saved * monthly_salary) 
    months = months + 1

print("Number of Months >>>: ", + months)
