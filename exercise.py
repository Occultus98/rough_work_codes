#DECLARATIONS
item_name = str(input("\nItem: "))
cost_price = float(input("Cost price: "))
transport_cost = float(input("Transport cost: "))

#COMPUTATIONS
selling_price = cost_price + (cost_price*0.05 + transport_cost*0.02)
profit = selling_price - cost_price

#OUTPUT
print(f"\nSelling Price:\t{selling_price}\nProfit Margin:\t{profit}\n")