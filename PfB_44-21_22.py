# Handling multiple conditions

if province == "Alberta" \
    or province == "Nunavut":
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15

# Truth Table
# First Condition   Second Condition    Condition evaluates as
# TRUE              TRUE                TRUE
# TRUE              FALSE               TRUE    
# FALSE             TRUE                TRUE
# FALSE             FALSE               FALSE


# IN Operator

if province in ("Alberta", "Nunavut", "Yukon"):
    tax = 0.05
elif province == "Ontario":
    tax = 0.12
else:
    tax = 0.15    

# Nested if statements

if country == "Canada":
    if province in ("Alberta", "Nunavut", "Yukon"):
        tax = 0.05
    elif province == "Ontario":
        tax = 0.12
    else:
        tax = 0.15
else:
    tax = 0.0  

