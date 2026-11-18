prices = {
    "apple": 20,
    "milk": 30,
    "bread": 25,
    "rice": 50,
    "sugar": 40
}

out_of_stock = ["milk", "sugar"]

order = ["apple", "milk", "bread", "rice"]
total = 0 

for item in order:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total = total + prices[item]

print(f"Total order:", total)