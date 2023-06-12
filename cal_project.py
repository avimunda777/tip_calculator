# Tip calculator
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places = 33.60
print('Welcome to the tip calculator!')
bill = float(input('What was the bill? $'))

tip = int(input('How much tip would you like to give? 10, 12, or 15?' ))
people = int(input('How many people to split the bill?'))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
