# Parameterized Functions

# This function will take a name and return the first
# letter of the name
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask for someone's name und return the initials

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name, False)

print("Your initial is: " + first_name_initial)

# Default uppercase

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask for someone's name und return the initials

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)

print("Your initial is: " + first_name_initial)


# Named Parameter

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask for someone's name und return the initials

first_name = input("Enter your first name: ")
first_name_initial = get_initial(force_uppercase=False, name=first_name)

print("Your initial is: " + first_name_initial)