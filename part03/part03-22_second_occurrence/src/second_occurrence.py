word = input("Please type in a string: ")
char = input("Please type in a substring: ")

first_index = word.find(char)

if first_index >= 0:
    chopped_word = word[first_index+len(char):]
    second_index = chopped_word.find(char)
    if second_index >= 0:
        index = first_index + second_index + len(char)
        print(f"The second occurrence of the substring is at index {index}.")
    else:
        print(f"The substring does not occur twice in the string.")
else:
    print(f"The substring does not occur twice in the string.")