print("Welcome to the tip calculator!")
total_bill = float(input("What was your total bill ? Rs "))
tip_percent = int(input("How much tip would you like to give ? 10, 12, or 15 ? "))
people = int(input("How many people to split the bill? "))

bill_each = round(((total_bill + ((tip_percent/100) * total_bill))/people),2)
print(f"Each person has to pay: Rs {bill_each}")