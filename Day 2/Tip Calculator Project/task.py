print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ : "))
tip = int(input("What percentage tip would you like to give? 10 12 15 : "))
people = int(input("How many people to split the bill? : "))

print("\nYour Split Bill Is : $"+str(round((bill/people)*1.12,2)))
