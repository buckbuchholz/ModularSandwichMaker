import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)  # Create an instance of SandwichMaker
cashier_instance = Cashier()  # Create an instance of Cashier

def main():
    while True:
        sandwich_size = input("What size sandwich would you like? (small/medium/large): ").lower()
        if sandwich_size in recipes:
            order_ingredients = recipes[sandwich_size]
            if sandwich_maker_instance.check_resources(order_ingredients["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, order_ingredients["cost"]):
                    sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients["ingredients"])
                    print(f"Here is your {sandwich_size} sandwich. Enjoy!")
                else:
                    print("Insufficient payment, please try again.")
            else:
                print("Sorry, there are not enough ingredients for your order.")
        else:
            print("Invalid size. Please choose small, medium, or large.")

if __name__ == "__main__":
    main()
