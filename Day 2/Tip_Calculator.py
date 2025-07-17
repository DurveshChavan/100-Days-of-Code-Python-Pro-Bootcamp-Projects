# based on your bill this program calculates the bill for each person

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n₹"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15 \n= "))
people = int(input("How many people to split the bill? \n"))

each_tip = (bill+(bill*(tip/100)))/people # keeping in mind the percentage

print(f"Each person should pay: ₹{round(each_tip, 2)}")



