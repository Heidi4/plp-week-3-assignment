def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price

def main():
    try:
        # Get input from user
        price = float(input("Enter the original price: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price
        final_price = calculate_discount(price, discount_percent)
        
        # Display results
        if discount_percent >= 20:
            print(f"\nDiscount of {discount_percent}% applied!")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main()
