"""
Used ChatGPT to:
- understand how file data can be converted into objects
- learn how object lists can be searched and updated
- improve menu-driven program structure
- format inventory data into readable table layouts
- debug object vs list attribute errors
- improve output readability using string formatting alignment
"""
#========The beginning of the class==========
class Shoe:  #creating class; remember to capitalize first letter

    def __init__(self, country, code, product, cost, quantity):  #Constructor
        self.country = country #attribute
        self.code = code #attribute
        self.product = product #attribute
        self.cost = cost #attribute
        self.quantity = quantity #attribute

     
    def get_cost(self): #method
        return self.cost #returns cost of shoe

    def get_quantity(self): #method
        return self.quantity #returns quantity of shoes in stock

    def __str__(self): #method
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost {self.cost}, Quantity {self.quantity}"
       


#=============Shoe list===========
'''
Object Inventory List.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:

            next(file)  # skips the first header line

            for line in file:

                country, code, product, cost, quantity = line.strip().split(",")

                shoe = Shoe(country, code, product, int(cost), int(quantity))

                shoe_list.append(shoe)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.txt was not found.")

    '''
    Function that:
    - Opens the file inventory.txt
    - Reads the data from this file
    - Creates a shoes object
    - Appends new object into the shoes list 
    '''
def capture_shoes():
    
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = int(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    new_shoe = Shoe(country, code, product, cost, quantity)

    shoe_list.append(new_shoe)

    print("Shoe added successfully.")
    
    '''
    Function allows a user to 
    - Capture data about a shoe
    - Use input data to create a shoe object
    - Append new object inside the shoe list (memory only; not updating file)
    '''

def view_all():
    print("\n{:<15} {:<12} {:<25} {:<10} {:<10}".format(
        "Country", "Code", "Product", "Cost", "Quantity"
    ))

    print("-" * 75)

    for shoe in shoe_list:

        print("{:<15} {:<12} {:<25} {:<10} {:>10}".format(
            shoe.country,
            shoe.code,
            shoe.product,
            shoe.cost,
            shoe.quantity
        ))

    '''
    Function iterates over the shoes list and print the details of the shoes 
    returned from the "__str__" function
    '''

def re_stock():
    lowest_shoe = shoe_list[0]

    for shoe in shoe_list:
        if shoe.quantity < lowest_shoe.quantity:
            lowest_shoe = shoe

    print("\nThis shoe has the lowest quantity:\n")
    print(lowest_shoe)

    answer = input("Do you want to add more stock? yes/no:  ").lower()
                   
    if answer == "yes":
        add_quantity = int(input("How many shoes do want to add? "))

        lowest_shoe.quantity += add_quantity

        with open("inventory.txt", "w") as file:

            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoe_list:

                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )


        print("Stock updated.")
        print(lowest_shoe)

    else:
        print("Stock was not updated.")
                   
    '''
    Function used to:
    - Find the shoe object with the lowest quantity; to be restocked
    - Ask the user if they want to restock
    - Make updates to inventory.
    - Updates quantity on the .txt file
    '''

def search_shoe():
    search_code = input("Enter shoe code to search: ")

    for shoe in shoe_list:

        if shoe.code == search_code:

            print("\n{:<15} {:<12} {:<30} {:<10} {:<10}".format(
                "Country", "Code", "Product", "Cost", "Quantity"
            ))

            print("-" * 90)

            print("{:<15} {:<12} {:<30} {:<10} {:<10}".format(
                shoe.country,
                shoe.code,
                shoe.product,
                shoe.cost,
                shoe.quantity
            ))

            return

    print("Shoe not found.")
    
    '''
     Function used:
    - Search for a shoe
    - Print shoe if found
    - Notify user if not found
    
    '''

def value_per_item():

    print("\n{:<30} {:<15} {:<15}".format(
        "Product", "Code", "Total Value"
    ))

    print("-" * 65)

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()

        print("{:<30} {:<15} {:>15}".format(
            shoe.product,
            shoe.code,
            value
        ))
    '''
    Function used to calculate the total value for each item.
    ''' 

def highest_qty():
    highest_shoe = shoe_list[0]

    for shoe in shoe_list:
        if shoe.quantity > highest_shoe.quantity:
            highest_shoe = shoe

    print("\nThis shoe is for sale:\n")

    print("{:<15} {:<12} {:<30} {:>10} {:>10}".format(
        "Country", "Code", "Product", "Cost", "Quantity"
    ))

    print("-" * 90)

    print("{:<15} {:<12} {:<30} {:>10} {:>10}".format(
        highest_shoe.country,
        highest_shoe.code,
        highest_shoe.product,
        highest_shoe.cost,
        highest_shoe.quantity
    ))

    
    '''
    Determine the product with the highest quantity
    '''

#==========Main Menu=============
'''
Menu to execute each function above.
'''

read_shoes_data()

while True:
    print("\nNike Warehouse Inventory Menu")
    print("1. View all shoes")
    print("2. Add new shoe")
    print("3. Restock lowest quantity shoe")
    print("4. Search shoe by code")
    print("5. View value per item")
    print("6. View shoe with highest quantity")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Goodbye.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")