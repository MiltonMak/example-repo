from tabulate import tabulate # Import the tabulate function from the tabulate module to display data in a table format

#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Add the code to return the cost of the shoe in this method.
    def get_cost(self):

        return self.cost

    # Add the code to return the quantity of the shoe in this method.
    def get_quantity(self):
        
        return self.quantity

    # Add a __str__() method that returns a string representation of a class.
    def __str__(self):

        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    
    # This function will read the data from the file inventory.txt

    with open('inventory.txt', 'r') as file:

        next(file) # Skip the first line

        # Use try-except to handle potential errors while reading the file
        try:
            for line in file:
                data = line.strip().split(',')
                shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                shoe_list.append(shoe)

        except Exception as e:
            print(f"Error reading shoe data: {e}")


# This function will allow a user to capture data about a shoe 
# and use this data to create a shoe object and append this object inside the shoe list.

def capture_shoes():

    input_country = input("Enter the country of the shoe: ")
    input_code = input("Enter the code of the shoe: ").upper() # Convert the input to uppercase to maintain consistency
    input_product = input("Enter the product name of the shoe: ")
    input_cost = float(input("Enter the cost of the shoe: "))
    input_quantity = int(input("Enter the quantity of the shoe: "))
    shoe = Shoe(input_country, input_code, input_product, input_cost, input_quantity)
    shoe_list.append(shoe)

    # Append the new shoe data to the inventory.txt file
    with open('inventory.txt', 'a') as file:
        file.write(f"{input_country},{input_code},{input_product},{input_cost},{input_quantity}\n")


def view_all():

    table_data = [] # Create an empty list to hold the table data
    for shoe in shoe_list:
        table_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    # Use the tabulate function to print the table with headers
    print("\nAll shoes in inventory:\n")
    print(tabulate(table_data, headers=["Country", "Code", "Product", "Cost", "Quantity"]))

def re_stock():
    # This function will find the shoe object with the lowest quantity, which is the shoe that needs to be re-stocked. 
    # Ask the user for input of how many shoes they would like to add and then update the quantity of that shoe object.

    # Find the shoe with the lowest quantity using the min function and a lambda function as the key
    lowest_shoe = min(shoe_list, key=lambda x: x.quantity) 
    print(f"\nShoe with lowest quantity: {lowest_shoe}\n")

    # Ask the user for input of how many shoes they would like to add and then update the quantity of that shoe object
    add_quantity = int(input("Enter the quantity to add: "))
    
    # add the new quantity to the existing quantity of the shoe object and update the shoe object with the new quantity on the text file
    lowest_shoe.quantity += add_quantity
    lowest_shoe_data = f"{lowest_shoe.country},{lowest_shoe.code},{lowest_shoe.product},{lowest_shoe.cost},{lowest_shoe.quantity}\n"
    with open('inventory.txt', 'r') as file:
        lines = file.readlines()

    # Find the line corresponding to the lowest shoe and update it
    for i, line in enumerate(lines):
        if lowest_shoe.code in line:
            lines[i] = lowest_shoe_data
            break

    # Write the updated lines back to the file
    with open('inventory.txt', 'w') as file:
        file.writelines(lines)

    print(f"\nUpdated quantity for {lowest_shoe}: {lowest_shoe.quantity}\n")

def search_shoe():
    # This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
    search_code = input("Enter the shoe code to search: ").upper() # Convert the input to uppercase to ensure case-insensitive search
    for shoe in shoe_list:
        if shoe.code == search_code:
            print("\nSearch result\n")
            print(f"result : {shoe}")
            return shoe

def value_per_item():
    # This function will calculate the total value for each item.
    # Please keep the formula for value in mind: value = cost * quantity.
    # Print this information on the console for all the shoes.
    print("\nValue per item:\n")
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: ${value}")

# This function will determine the shoe with the highest quantity and print this shoe as being for sale.
def highest_qty():

    # Find the shoe with the highest quantity using the max function and a lambda function as the key
    highest_shoe = max(shoe_list, key=lambda x: x.quantity) 
    print(f"\nShoe with highest quantity: \n"
          f"\n{highest_shoe} is for Sale Now!")
    
def remove_shoe():
    # This function will remove a shoe from the list using the shoe code and then update the text file.
    remove_code = input("Enter the shoe code to remove: ").upper() # Convert the input to uppercase to ensure case-insensitive search
    for shoe in shoe_list:
        if shoe.code == remove_code:
            shoe_list.remove(shoe) # Remove the shoe from the list
            print(f"\nShoe with code {remove_code} has been removed.\n")
            break

    # Update the text file after removing the shoe
    with open('inventory.txt', 'w') as file:
        file.write("Country,Code,Product,Cost,Quantity\n") # Write the header line
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n") # Write each shoe's data to the file

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

def main_menu():

    while True:
        print("\nMain Menu\n"
            "1. Capture shoe data\n"
            "2. View all shoes\n"
            "3. Re-stock shoe\n"
            "4. Search shoe\n"
            "5. Calculate value per item\n"
            "6. Show shoe with highest quantity\n"
            "7. Remove shoe\n"
            "8. Exit")

        choice = input("Enter your choice number (1-8): ")

        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            remove_shoe()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

#========The main program starts here=========

# Read the shoe data from the file and populate the shoe list
read_shoes_data()

# Call the main menu function to start the program
main_menu()