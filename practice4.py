
book_type = input("Enter book type (standard/reference): ")
days = int(input("Enter overdue days: "))
premium = input("Are you a premium member? (yes/no): ")

if book_type == "standard":
    if days <= 5:
        fine = days * 5
    else:
        fine = (5 * 5) + (days - 5) * 10

elif book_type == "reference":
    fine = days * 20

else:
    fine = 0
    print("Invalid book type")

if book_type == "standard" or book_type == "reference":
    if premium == "yes":
        fine = fine - (fine * 20 / 100)

    print("Total fine: Rs", fine)
