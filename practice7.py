age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
alone = input("Traveling alone? (yes/no): ")
tatkal = input("Is it a Tatkal booking? (yes/no): ")
festival = input("Is it a festival season? (yes/no): ")

if (age <= 60 or (gender == "F" and alone == "yes")) and tatkal == "no" and festival == "no":
    print("You are eligible for a discount on your train ticket.")
else:
    print("You are not eligible for a discount on your train ticket.")    






























































