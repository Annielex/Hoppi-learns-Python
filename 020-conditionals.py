# Multiple Conditions

if province == "Alberta" \
or province == "Nunavut":
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15

# Truth table for OR:
#   first condition   second condition    condition evaluates as
#   TRUE                TRUE                TRUE
#   TRUE                FALSE               TRUE
#   FALSE               TRUE                TRUE
#   FALSE               FALSE               FALSE

# IN operator

if province in("Alberta", \
               "Nunavut", "Yukon"):
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15
