class Cellphone:
    def __init__(self, model, brand, price, quantity):
        self.model = model
        self.brand = brand
        self.price = price
        self.quantity = quantity

class OnlineStore:
    def __init__(self):
        self.cellphones = []

    def add_cellphone(self, cellphone):
        self.cellphones.append(cellphone)

    def display_cellphones(self):
        print("Available Cellphones:")
        for index, cellphone in enumerate(self.cellphones, start=1):
            print(f"{index}. {cellphone.brand} {cellphone.model} - ${cellphone.price} ({cellphone.quantity} available)")

    def sell_cellphone(self, index, quantity):
        selected_cellphone = self.cellphones[index - 1]

        if selected_cellphone.quantity >= quantity:
            total_cost = selected_cellphone.price * quantity
            print(f"Total cost: ${total_cost}")
            selected_cellphone.quantity -= quantity
            print(f"You have successfully purchased {quantity} {selected_cellphone.brand} {selected_cellphone.model}(s)!")
        else:
            print("Sorry, the selected quantity is not available.")

# Sample usage
if __name__ == "__main__":
    online_store = OnlineStore()

    cellphone1 = Cellphone("iPhone 12", "Apple", 999, 5)
    cellphone2 = Cellphone("Galaxy S21", "Samsung", 899, 8)
    cellphone3 = Cellphone("Pixel 5", "Google", 699, 10)

    online_store.add_cellphone(cellphone1)
    online_store.add_cellphone(cellphone2)
    online_store.add_cellphone(cellphone3)

    while True:
        print("\nWelcome to the Online Cellphone Store!")
        online_store.display_cellphones()

        try:
            choice = int(input("Enter the cellphone number you want to buy (0 to exit): "))
            if choice == 0:
                break
            elif 0 < choice <= len(online_store.cellphones):
                quantity = int(input("Enter the quantity you want to buy: "))
                online_store.sell_cellphone(choice, quantity)
            else:
                print("Invalid cellphone number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Thank you for shopping with us!")
