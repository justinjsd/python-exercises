# Write your solution here# Write your solution here

def no_shouting(my_list: list):
    pruned_list = []
    for elem in my_list:
        if elem.isupper() == False:
            pruned_list.append(elem)
    return pruned_list

if __name__ == "__main__":
    print(no_shouting(['FIRST', 'second', 'THIRD', 'fourth']))