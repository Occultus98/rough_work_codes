#INPUTS AND DECLARATIONS
employee_name = input("Enter name: ")
hours_worked = float(input("Enter Hours Worked: "))
overtime_pay = 0
BASIC_RATE = 4.00

#COMPUTATIONS
if hours_worked <= 40:
    BASIC_RATE = 4.00
elif hours_worked > 40:
    over_time = hours_worked - 40
    overtime_pay_rate = 2.00
    overtime_pay = over_time * 2.00
basic_pay_rate  = hours_worked * BASIC_RATE
total = basic_pay_rate + overtime_pay
    
#OUTPUT
print(f"EMPLOYEE NAME: {employee_name}\nBASIC RATE PAY: {basic_pay_rate}\nOVERTIME PAY: {overtime_pay}\nTOTAL PAY: {total}")