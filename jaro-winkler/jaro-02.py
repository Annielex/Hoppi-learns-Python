# Write a small python script, that accepts two input strings (mixed case), and compares them:
# - lowercase compare
# - by counting the number characters that both strings have in common (place independent)
# - remember the order of common characters for both strings

input_A = "aPpLE"
input_P = "PeAcH"

print(f"This script shall compare {input_A.lower()} and {input_P.lower()}.")

List_C = [input_A.lower(), input_P.lower()] 

print(List_C)

Matrix_C = list(map(list, List_C))

print(Matrix_C)