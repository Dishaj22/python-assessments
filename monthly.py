
pocket_money = float(input("Enter monthly pocket money: "))

canteen = float(input("Enter canteen expense: "))
transport = float(input("Enter transport expense: "))
shopping = float(input("Enter shopping expense: "))

total_expense = canteen + transport + shopping

savings = pocket_money - total_expense

is_budget_safe = savings >= 0

print("Pocket money:", pocket_money)
print("Total expense:", total_expense)
print("Remaining savings:", savings)
print("Budget safe:", is_budget_safe)
