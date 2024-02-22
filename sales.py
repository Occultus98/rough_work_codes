#DECLARATIONS
sales_person_name = input("Name: ")
id_number = input("Id Number: ")
weekly_total_sales = int(input("Weekly Total Sales: "))
base_pay = 1000000

#COMPUTATIONS
if weekly_total_sales <= 5000000:
    commission = weekly_total_sales * 0.1
elif weekly_total_sales > 5000000:
    sales_beyond = weekly_total_sales - 5000000
    commission = (5000000 * 0.1) + (sales_beyond * 0.15)
pay = base_pay + commission

#OUTPUT
print(f"\n\n\tNAME:\t\t{sales_person_name}\n\tID NUMBER:\t{id_number}\n\tPAY:\t\t{pay}\n")