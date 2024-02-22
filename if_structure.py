#DECLARATIONS
employee_name = input("\nEmployee Name: ")
hours_worked = int(input("Hours Worked: "))
RATE = 30000
TAXED_WAGE = 500000

#COMPUTATIONS
wage = hours_worked * RATE

if wage > TAXED_WAGE:
    print('\n\t"SEBO OJJA KUSASULA OMUSOLO OSAAGA"\n')
    tax = 0.1 * wage
else:
    print('\n\t"NOT ELIGIBLE TO PAY TAX"\n') 
    tax = 0
net_wage = wage - tax   
print(f"\nWAGE:{wage}\nNET WAGE:{net_wage}\n")
