print("Welcome to the tip calculator.")

total_bill = float(input("What was total bill? $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

percentage_tip_float = percentage_tip/100

number_people = int(input("How many people to split the bill?"))

value_per_person = (total_bill * (1.00 + percentage_tip_float)/ number_people)

value_per_person = round(value_per_person,2)
value_per_person = "{:.2f}".format(value_per_person)

print(f"Each person should pay: ${value_per_person}")

