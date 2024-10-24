supplyDemandData = {
    "apples": {
        "supply": lambda x: 10 + 2 * x,
        "demand": lambda x: max(0, 50 - 3 * x),
    },
    "bananas": {
        "supply": lambda x: 15 + 1.5 * x,
        "demand": lambda x: max(0, 30 - 2 * x),
    },
}

def simulate_supply_demand():
    print("Welcome to the Supply and Demand Simulator!")
    print("You can explore how changes in supply and demand affect prices!")
    print("Available products: apples, bananas")

    product = input("Which product do you want to simulate? (apples, bananas) ").lower()

    if product in supplyDemandData:
        try:
            quantity = int(input("Enter the quantity for the simulation: "))
        except ValueError:
            print("Please enter a valid number for the quantity.")
            return

        supply = supplyDemandData[product]["supply"](quantity)
        demand = supplyDemandData[product]["demand"](quantity)

        if supply == demand:
            print(f"The equilibrium price for {product} at quantity {quantity} is {supply}.")
        elif supply > demand:
            print(f"The market is oversupplied for {product}. The price will likely decrease to {demand}.")
        else:
            print(f"The market is undersupplied for {product}. The price will likely increase to {supply}.")
    else:
        print("Hmm, I don't know that product. Try apples or bananas!")

while True:
    try:
        simulate_supply_demand()
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
    finally:
        playAgain = input("Do you want to simulate supply and demand again? (yes/no) ").lower()
        if playAgain != "yes":
            print("Thanks for using the Supply and Demand Simulator! Goodbye!")
            break