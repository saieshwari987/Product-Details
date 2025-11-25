# product_details.py
def format_product_details(product_id, name, quantity, price):
    """
    Returns a well-formatted string with product details.
    """
    result = (
        "Product Details\n"
        f"Product ID   : {product_id}\n"
        f"Name         : {name}\n"
        f"Quantity     : {quantity}\n"
        f"Price        : {price}"
    )
    return result

def main():
    # Sample fixed data (no user input)
    product_id = "P1001"
    name = "Pen Drive"
    quantity = 3
    price = 499

    formatted_info = format_product_details(product_id, name, quantity, price)

    print(formatted_info)

if __name__ == "__main__":
    main()