# Write your solution here

def list_sum(l1: list, l2:list):
    i = 0
    l3 = []
    for elem in l1:
        l3.append(l1[i] + l2[i])
        i += 1
    return l3

if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    print(list_sum(l1, l2))
                           