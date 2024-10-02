print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + (int(tip)/100))
each_pay = round((total_bill / people),3)
print(f"Each person pays: {each_pay}")