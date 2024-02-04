# AND statements processing
#   First Condition   Second Condition    Condition evaluates as
#   TRUE                TRUE                TRUE
#   TRUE                FALSE               FALSE
#   FALSE               TRUE                FALSE
#   FALSE               FALSE               FALSE

# A student makes honour roll if their average is >=85
# and their lowest grade is not below 70
gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))

#if gpa >= .85:
#    if lowest_grade >= .70:
#        print("You made honour roll")


#if gpa >= .85 and lowest_grade >= .70:
#    print("You made honour roll!")

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code if you need to check if student is
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
    print("You made honour roll")
