# Functions

# Functions make your code more readable and easier to maintain.
# Always add comments to explain the purpose of your functions.
# Functions must be declared before the line of code where the
# function is called.

# Function to print current date and time
#from datetime import datetime

#def print_time(task_name):
#    print(task_name)
#    print(datetime.now())
#    print()

# print timestampt to see how long sections of code
# take to run.

#first_name = "Susan"
# replacing the following code with function
#print("task completed")
#print(datetime.datetime.now())
#print()

#print_time("printed first name")

#for x in range (0,10):
#    print(x)
#print_time("completed for loop")

# Function for returning initials
# This function returns the first initial of a name

def get_initial(name: str) -> str:
    initial = name[0:1].upper()
    return initial

# Ask for someone's name and return their initials
first_name = input("Enter your first name: ")
# replacing code with function:
#first_name_initial = first_name[0:1]
first_name_initial = get_initial(first_name)

middle_name = input("Enter your middle name: ")
# replacing code with function:
#middle_name_initial = middle_name[0:1]
middle_name_initial = get_initial(middle_name)

last_name = input("Enter your last name: ")
# replacing code with function:
#last_name_initial = last_name[0:1]
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial \
      + middle_name_initial + last_name_initial)