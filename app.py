def calculate_discount(price ,discount):
    if discount > 20:
        return(price - price*20/100)
    elif discount < 20:
        return (price)

price=float(input("enter price the original price"))
discount_price=float(input("enter the discount percentage"))
final_price = calculate_discount(price, discount_price)
print(f"The final price is: {final_price}")
