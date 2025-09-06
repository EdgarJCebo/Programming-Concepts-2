def calculate_discount(price, discount_rate):
    # Calculate the discount amount based on the price and discount rate.
    discount_amount = price * discount_rate
    return discount_amount

def apply_discount(price, discount_amount):
    # Apply the discount amount to the original price and return the new price.
    new_price = price - discount_amount
    return new_price

def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = product["price"]
            discount_rate = product["discount_rate"]

            # Converting the string prices to float if needed
            if isinstance(price, str):
                price = float(price)

            # Making sure the discount_rate is a number
            if not isinstance(discount_rate, (int, float)):
                raise TypeError(f"Invalid discount_rate: {discount_rate}")

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price:.2f}")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price: ${final_price:.2f}")
            print()

        # Excepting the exception given in the code
        except Exception as e:
            print(f"Error processing product {product.get('name', 'Unknown')}: {e}")
            print()

if __name__ == "__main__":
    main()
