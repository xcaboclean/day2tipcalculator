print("Welcome to the tip calculator.")
total_bill = float(input("\nWhat was total bill? $"))
percentage_tip = int(input("\nWhat perentage tip would you like to give? 10, 12 or 15"))
number_people = int(input("\nHow many people to split the bill?"))
bill_per_person = total_bill(1 + (percentage_tip/100))/number_people

print(f"Each person should pay{bill_per_person}.2")
