# Write your solution here

def distinct_numbers(l: list):
    dl = []
    for i in range(len(l)):
        if l[i] not in l[i+1:]:
            if l[i] in dl:
                continue
            else:
                dl.append(l[i])
    return sorted(dl)

if __name__ == "__main__":
    l = [5, 6, 7, 8, 8, 9, 9, 5]
    print(distinct_numbers(l))


                           