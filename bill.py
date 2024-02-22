#DECLARATIONS
distance = int(input("\nDistance covered(km): "))


if distance < 0:
    print("Distance cannot be in negative, Enter positive number please!\nAnyways..........")
if distance < 10:
    rate = 5000
elif distance < 50:
    rate = 10000
else:
    rate = 15000
bill = distance * rate
print(f"For a distance of {distance} kilometres, the bill is {bill}.\n")




