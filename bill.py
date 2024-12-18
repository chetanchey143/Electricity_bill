def calculate_bill(units):
    rate1 = 0.45  # for the first 50 units
    rate2 = 0.65  # for the next 100 units
    rate3 = 1.00  # for the next 150 units
    rate4 = 1.55  # for the next 200 units
    rate5 = 1.75  # for the next 250 units
    rate6 = 2.00  # for more than 250 units

    total_bill = 0

    if units <= 50:
        total_bill = units * rate1
    elif units <= 100:
        total_bill = 22.50 + (units * rate2)
    elif units <= 150:
        total_bill = 87.50 + (units * rate3)
    elif units <= 200:
        total_bill = 237.50 + (units * rate4)
    elif units <= 250:
        total_bill = 547.50 + (units * rate5)
    else:
        total_bill = 985 + (units * rate6)
    
    total_bill_with_additional = total_bill + (total_bill * 0.10)
    
    return total_bill_with_additional
units = float(input("Enter the number of electricity units consumed: "))

# Calculate the total bill
total_amount = calculate_bill(units)

# Display the total bill
print(f"The total electricity bill is Rs {total_amount:.2f}")