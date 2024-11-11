# Write your solution here

def most_common_character(string):
    i = len(string) - 1
    most = 0
    while i >= 0:
        if string.count(string[i]) > most:
            most = string.count(string[i])
            common = string[i]
            i -= 1
    return common

if __name__ == "__main__":
    print(most_common_character("aabbbbc"))