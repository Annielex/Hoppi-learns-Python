# # Error Handling

# # Error handling is not the same as Debugging
# # Error handling is external issues with the code that was not predicted to go sidewazs
# # Debugging is knowing the code is behaving correctly but not the intended way 

# # Syntax errors
# # This code won't run:
# x = 42
# y = 206
# if x == y
#     print("Success!!")

# Runtime errors
# This code will fail when run (division by zero)
x = 42
y = 0
#print(x/y)
#print("da")

# Catching runtime errors
#try:
#        print(x/y)
#        print(f"f = {x}/{y}")
#except ZeroDivisionError as e:
#        # Optionally. log e somewhere
#        print(f"Sorry, something went wrong: y = {y}")
#        #raise e
#else:
#        print(f"Something really went wrong by doing {x}/{y}")
#finally:
#        print("This always runs on success or failure")                

#print("da")
# try, except, finally is not used to find bugs
# (debugging is not error handling)

# You don't have to catch all errors
# Let it bubble up, someone else will deal with it
# the application will crash: sometimes this is exactly what you want

#try:
#        pass
#except expression as identifier:
#        pass
#else:
#        pass
#finally:
#        pass
#print()



# Logic errors
# This code won't run at all
x = 206
y = 42
if x < y:
# logic error: meant to write if x > y
        print(str(x) + " is greater than " + str(y))

#Figuring out what went wrong:
#Stack trace
#      last calls are on top
#   your code is likely on the bottom
#   seek out line number
# Finding your mistake
#   Reread code
#   check documentation
#   search internet
#   take a break
#   ask someone for help
