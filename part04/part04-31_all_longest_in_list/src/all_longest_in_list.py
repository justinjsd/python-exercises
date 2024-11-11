# Write your solution here

def all_the_longest(l: list):
    longest = 0
    new_list = []
    for elem in l:
        if len(elem) > longest:
            longest = len(elem)

    for elem in l:
        if len(elem) == longest:
            new_list.append(elem)

    return new_list
 
if __name__ == "__main__":
    print(all_the_longest(["ab", "bc", "cdf", "efg", "a"]))