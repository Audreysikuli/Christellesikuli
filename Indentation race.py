# Challenge 1: Even and Odd Numbers
def main():
    print("welcome to the Indentation Race!")
    for i in range(5):
        print("Current number:", i)
        if i % 2 == 0:
           print("Even number.")
        else:
           print("Odd number.")
    print("Race completed!")

# Challenge 2: Total cost Calculator
def calculate_total_price(item_price, quantity):
    item_total = item_price * quantity
    tax_rate = 0.07
    tax_amount = item_total * tax_rate
    total_price = item_total + tax_amount
    discount = 0.1
    discounted_price = total_price - (total_price * discount)
    return discounted_price

main()
item_price = 25.0
quantity = 4
print("Total price:", calculate_total_price(item_price, quantity))
