def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount.
    """
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Print result
if final_price != original_price:
    print(f"The final price after applying the discount is ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is ${original_price:.2f}")
