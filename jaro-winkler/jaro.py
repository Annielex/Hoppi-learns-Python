# Write a small python script, that accepts two input strings (mixed case), and compares them:
# - lowercase compare
# - by counting the number characters that both strings have in common (place independent)
# - remember the order of common characters for both strings

input_1 = "apple" # input("Please enter a mixed case letter string: ")
input_2 = "peach" # input("Please enter another mixed case letter string: ")

print(f"Comparing {input_1.lower()} and {input_2.lower()}")

string_1 = list(input_1)
string_2 = list(input_2)


common_1 = list()
common_2 = list()

count_same = 0

for i in range(len(string_1)):
    # print(string_1[i])
    for j in range(len(string_2)):
        # print(string_2[j])
        if string_1[i] == string_2[j]:
            count_same = count_same + 1
            string_2[j] = "_"
            common_1.append(string_1[i])
            break

string_2 = list(input_2)

for j in range(len(string_2)):
    for i in range(len(string_1)):
        if string_1[i] == string_2[j]:
            string_1[i] = "_"
            common_2.append(string_2[j])
            break

print(count_same)
print(common_1)
print(common_2)


