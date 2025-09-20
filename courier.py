

insurance = input("Please choose your insurance (full or limited): ")
if insurance == "full":
    insurance_cost = 50.00
else:
    insurance_cost = 25.00

gift = input("Would you like to include a gift? (yes or no): ")
if gift == "yes":
    gift_cost = 15.00
else:
    gift_cost = 0.00

priority = input("Please choose your delivery priority (priority or standard): ")
if priority == "priority":
    priority_cost = 100.00
else:
    priority_cost = 20.00

total_cost = package_price + delivery_cost + insurance_cost + gift_cost + priority_cost
print("The total cost of your package is $" + str(total_cost))