#DISPLAY PAGE
print('''\n\tEMPLOYEE CATEGORIES\n
1. Managers
2. Hourly Workers
3. Commission Workers
4. Piece Workers
''')

#COMPUTATIONS AND INPUTS
category_code = int(input("Choose Your Category: "))
category_name = ""
if category_code == 1:
    category_name = "Managers"
    weekly_pay = 20000
elif category_code == 2:
    category_name = "Hourly Workers"
    hours_worked = int(input("Hours Worked: "))
    if hours_worked < 40:
        basic_hourly_wage = 300 
        weekly_pay = hours_worked * basic_hourly_wage
    elif hours_worked > 40:
        basic_hourly_wage = 300
        basic_pay = basic_hourly_wage * 40
        extra_hours = hours_worked - 40
        weekly_pay = basic_pay + (extra_hours * 1.5)
    else:
        print("INVALID INPUT")
elif category_code == 3:
    category_name = "Commission Workers"
    pay_rate = 250
    gross_weekly_sales = int(input("Enter Gross Weekly Sales: "))
    weekly_pay = pay_rate + (gross_weekly_sales * 5.7/100)
elif category_code == 4:
    category_name = "Piece Workers"
    number_of_item_produced = int(input("Enter Number of Item(s) produced: "))
    type_of_item = int(input("How many Item type(s): "))
    if type_of_item == 1:
        rate = 200
        weekly_pay = number_of_item_produced * rate
    else:
        print("\nEach piece worker works on only one type of Item!")
        weekly_pay = 0
else:
    print('\n"INVALID CATEGORY CODE!"')
    weekly_pay = 0
    
#OUTPUT
print(f"\nCATEGORY: {category_name}\nWEEKLY PAY: {weekly_pay}\n")





