# Tip calculator
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places = 33.60

def calculate_tip(total_bill, num_people, tip_percentage):
    # Calculate the amount each person should pay
    amount_per_person = (total_bill / num_people) * (1 + tip_percentage/100)
    # Round the result to 2 decimal places
    amount_per_person = round(amount_per_person, 2)
    
    return amount_per_person
# Example usage
total_bill = 150.00
num_people = 5
tip_percentage = 12

amount_per_person = calculate_tip(total_bill, num_people, tip_percentage)
print(amount_per_person)