bill = float (input("Enter the total bill : "))
friend = int (input("Enter the number of friends : "))

tip = bill * 10 / 100
total = bill + tip

each_person = total / friend

print("original bill :", bill)
print("tip :", tip)
print("total :", total)
print("each person :", each_person)