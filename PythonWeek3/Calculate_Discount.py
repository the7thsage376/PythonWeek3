#Function used to calculate the discount om store items

def calculate_discount(price,discount):
        if discount >=20:
            discount_amount=price * (discount/100)
            discount_price=price - discount_amount
            return f'Price={discount_price}'
        else:
            return f'Price={price}'

#prompting the user to enter the price and discount
print(calculate_discount(price=float(input("Enter the price: ")),discount=float(input("Enter the discount: "))))
# I did it!
# I can code! :)