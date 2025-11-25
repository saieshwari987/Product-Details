# test_productdetails.py

from productdetails import format_product_details

def test_format_product_details():
    # Sample test data
    product_id = "P101"
    name = "Notebook"
    quantity = 5
    price = 50

    expected_output = (
        "Product Details\n"
        "Product ID   : P101\n"
        "Name         : Notebook\n"
        "Quantity     : 5\n"
        "Price        : 50"
    )

    assert format_product_details(product_id, name, quantity, price) == expected_output