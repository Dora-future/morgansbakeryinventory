# morgansbakeryinventory
Bakery Inventory System in Python
from datetime import datetime

# Ingredient and Product Data

ingredients = {

    "Flour": {"unit": "kg", "cost_per_unit": 0.8, "quantity": 100},
    "Sugar": {"unit": "kg", "cost_per_unit": 1.2, "quantity": 50},
    "Butter": {"unit": "kg", "cost_per_unit": 3.5, "quantity": 20},
    "Eggs": { "unit": "pcs", "cost_per_unit": 0.2, "quantity": 100},
    "BakingPowder": {"unit": "sachet" , "cost_per_unit": 0.1, "quantity": 100},
    "OliveOil" : {"unit": "litre", "cost_per_unit": 1.0, "quantity": 1},
    "Salt": {"unit": "kg", "cost_per_unit" : 0.85, "quantity": 20},
    "Milk": {"unit": "litre" , "cost_per_unit": 1.20, "quantity": 50},
    "Cinnamon": {"unit": "kg", "cost_per_unit": 2.50, "quantity" : 10},
    "VanillaPod": {"unit": "pod" , "cost_per_unit": 0.50, "quantity": 70},
    "Yeast": {"unit": "sachet" , "cost_per_unit": 0.20, "quantity": 0},
    
    
    
}

products = {
    "Muffin": {
        "price": 2.5,
        "recipe": {"Flour": 0.1, "Sugar": 0.05, "Butter": 0.05, "Eggs": 1}
    },

    "Bread": {
        "price": 1.8,
        "recipe": {"Flour": 0.25, "Salt":0.005, "OliveOil": 0.007, }
        },
    
    "American_pancake": {
        "price": 1.1,
        "recipe": { "Flour": 0.10, "Butter": 0.01, "Eggs":2, }
        
    }
}


sales_log = []
        



# Display ingredients

def show_ingredients():

    print("\n Ingredients Stock:")

    for name, data in ingredients.items():

        print(f"{name}: {data['quantity']} {data['unit']} (Cost/unit: £{data['cost_per_unit']})")



# Display products

def show_products():

    print("\n Bakery Products:")

    for name, data in products.items():

        print(f"{name}: £{data['price']}")

        print("  Ingredients:")

        for ing, amt in data['recipe'].items():

            unit = ingredients[ing]['unit']

            print(f"    - {ing}: {amt} {unit}")



# The sale

def sell_product(product_name, quantity):

    if product_name not in products:

        print("ERROR !!! Product not found in the system.")

        return



    recipe = products[product_name]["recipe"]



    # Check ingredient availability

    for ing, amt in recipe.items():

        required = amt * quantity

        if ingredients[ing]["quantity"] < required:

            print(f" ATTENTION PLEASE ! Not enough {ing} in stock! Please order products from the supplier")

            return



    # Deduct ingredients

    for ing, amt in recipe.items():

        ingredients[ing]["quantity"] -= amt * quantity

    # Sales of Restaurant ------------------------------------------

    sale = {

        "product": product_name,

        "quantity": quantity,

        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }

    sales_log.append(sale)

    total_price = products[product_name]["price"] * quantity

    print(f"Sold {quantity} {product_name}(s) for £{total_price:.2f}")



# Show sales

def show_sales():

    print("\n Morganas Bakery Sales Log:")

    for sale in sales_log:

        print(f"{sale['date']}: {sale['quantity']} x {sale['product']}")



# Morgans Bakery Main Menu

def main():

    while True:

        print("\n Morgan's Bakery Inventory System ")
        print("1. Ingredients")
        print("2. Products")
        print("3. Sell Product")
        print("4. View Sales ")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            show_ingredients()

        elif choice == "2":

            show_products()

        elif choice == "3":

            name = input("Enter product name to sell: ")

            qty = int(input("Enter quantity: "))

            sell_product(name, qty)

        elif choice == "4":

            show_sales()

        elif choice == "5":

            print("Thank you for using Morganas Bakery Inventory System")

            break

        else:

            print(" ERROR ! Inappropiate invalid choice or out of stock.")



if __name__ == "__main__":

    main()
