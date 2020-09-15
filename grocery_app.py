list_of_stores = []

#classes
class Grocery:
    def __init__(self, name):
        self.name = name
        self.address = None
        self.list = []

class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

class Item:
    def __init__(self, title, price, quantity):
        self.title = item
        self.price = price
        self.quantity = quantity
    
   
#add to shopping list
while True:
    task = input("""what would you like to do:
        1: Add store to the list
        2: Add item to a list
        3: View Lists
        4: Quit
        """)

    if task == "1":
        store_name = input("Enter the store name: ")
        print("Please enter address:")
        street = input("Street address: ")
        city = input("City: ")
        state = input("State: ")
        zip = input("Zip: ")
        
        store = Grocery(store_name)
        list_of_stores.append(store)
        
        full_address = Address(street, city, state, zip)
        store.address = full_address
        
        
          
    elif task == "2":
        print("***Stores***")
        for index in range(0, len(list_of_stores)):
            store_name = list_of_stores[index].name
            print(index, store_name)
        store_index = int(input("Enter the number of the store: "))
        item = input("Add item to shopping list: ")
        price = input("What is the price: ")
        quantity = input("What quantity: ")

        new_item = Item(item, price, quantity)
        list_of_stores[store_index].list.append(new_item)  
           
    elif task == "3":
        for i in range(0, len(list_of_stores)):
                store_name = list_of_stores[i].name
                shopping_list = list_of_stores[i].list[i].title
                cost = list_of_stores[i].list[i].price
                quantity = list_of_stores[i].list[i].quantity
                print(store_name, shopping_list, cost, quantity)
                
    elif task == "4":
        break
    else:
        print("That is not a valid option.")

print("Goodbye") 