from chicken import Chicken
from chickens import Chickens

menu_options = ["Exit", "Print Records", "Create New Record", "Update Existing Record", "Delete Record"]

def menu():
    id = 0
    for option in menu_options:
        print(f"{id}: {option}")
        id += 1

# Function for creating a new chicken with passed string
def add_chicken(chickens_object):
    name = input("Please input the new chicken's name")
    chickens_object.add_chicken(Chicken(name))

# Function for change the name of an existing chicken with passed index and new name string
def change_name(chickens_object):
    id = input("Please enter index number for the chicken you would like to modify\n")
    id = int(id)
    new_name = input("Please enter the new name\n")

    chickens_object.change_name(id, new_name)

def delete_chicken(chickens_object):
    id = input("Please enter the index number for the chicken you would like to delete\n")
    id = int(id)

    chickens_object.remove_chicken(id)

chickens = Chickens()

while(True):
    menu() # Call menu function, to print all available menu options

    selection = input("Please choose one of the options\n") # Accept user input for menu options
    selection = int(selection) # cast the input string to integer

    match selection:
        case 0:
            break
        case 1:
            chickens.print_chickens()
        case 2:
            add_chicken(chickens)
        case 3:
            chickens.print_chickens()
            change_name(chickens)
        case 4:
            chickens.print_chickens()
            delete_chicken(chickens)
        case _:
            print("Invalid choice, please try again")
