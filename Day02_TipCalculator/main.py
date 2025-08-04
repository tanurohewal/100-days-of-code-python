print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip/100*bill+bill
divided_tip = bill_with_tip/people
Total_round_of_bill = round(divided_tip)
print(f"Each person should pay:${Total_round_of_bill}")