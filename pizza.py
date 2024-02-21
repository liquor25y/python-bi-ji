def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

def show_pizza(toppings):
    print("here are your pizza's toppings")
    print(toppings)
