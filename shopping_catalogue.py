class Catalogue:
    def __init__(self):
        self.toys = ["spider-man", "batman", "football", "lego", "playing-cards"]
        self.washing_machine = ["beko", "samsung", "lg", "bosch", "indesit", "hotpoint", "hoover"]
        self.pc = ["hp", "siemens", "asus", "acer", "mac_book"]
        self.mobile_phone = ["samsung-phone", "iphone", "oneplus", "googlepixel", "nokia", "sony-ericsson"]
        self.shopping_basket = []


    def view_catalogue(self):
        for i in self.toys, self.washing_machine, self.pc, self.mobile_phone:
            print(i)

    def add_to_basket(self):
        product = input("Please add the product from toy's catalogue: ")
        if product in self.toys:
            self.shopping_basket.append(product)
            print(f"{product}, added to the basket")
        else:
            print("Sorry not available..")
        product = input("Please add the product from washing machine catalogue: ")
        if product in self.washing_machine:
            self.shopping_basket.append(product)
            print(f"{product}, added to the basket")
        else:
            print("Sorry not available..")
        product = input("Please add the product from PC catalogue: ")
        if product in self.pc:
            self.shopping_basket.append(product)
            print(f"{product}, added to the basket")
        else:
            print("Sorry not available..")
        product = input("Please add the product from Mobile Phone catalogue: ")
        if product in self.mobile_phone:
            self.shopping_basket.append(product)
            print(f"{product}, added to the basket")
        else:
            print("Sorry not available..")
        print(f"My shopping basket: {self.shopping_basket}")

    def remove_product_basket(self):
        r_product = input("Please type the item, you would like to remove: ")
        if r_product in self.shopping_basket:
            self.shopping_basket.remove(r_product)
            print(f"Product name {r_product}, has been removed from the shopping basket".title())
            print(f"Updated list after removing item: {self.shopping_basket}".title())
        else:
            print("Product is not available in the basket to delete.")

    def update_shopping_basket(self):
        update = input("Please type the item you would like to add from the catalogue: ")
        self.shopping_basket.insert(0, update)
        print(f"{update}, Item added to the basket.")
        print(f"Updated list: {self.shopping_basket}")


class User:
    def __init__(self):
        self.customers = {}
        self.catalogue = Catalogue()


    def register(self):
        r_first_name = input("Enter your Name: ")
        r_last_name = input("Enter your Last Name: ")
        self.customers[r_first_name] = r_last_name
        print("Registration Successful!!")

    def login(self):
        x = input("Enter your first name: ")
        y = input("Enter your last name: ")
        if x in self.customers.keys() and y in self.customers.values():
            print(f"{x}, Logged in")
        else:
            print("Incorrect, Please log in with your correct details..")


    def log_out(self):
        for key, value in self.customers.items():
            print(f"{key}, Logged out!!")
        print("Thank you for shopping, Goodbye!!")



user1 = User()
user1.register()
user1.login()
user1.catalogue.view_catalogue()
user1.catalogue.add_to_basket()
user1.catalogue.update_shopping_basket()
user1.catalogue.remove_product_basket()
user1.log_out()