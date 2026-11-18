item1 = float(input("Enter the first item price: "))
item2 = float(input("Enter the second item price: "))

total = item1 + item2

discount = total * 15 /100

delivery = 99

final_bill = total - discount + delivery

print("Item 1 :", item1)
print("Item 2 :", item2)
print("Total :", total)
print("Discount :", discount)
print("Delivery Charges :", delivery)
print("Final Bill :", final_bill)
