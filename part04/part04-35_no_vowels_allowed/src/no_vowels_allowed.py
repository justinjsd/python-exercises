# Write your solution here

def no_vowels(my_string):
    vowels = ["a","e","i","o","u"]
    word = ""
    for i in my_string:
        if i in vowels:
            i = ""
        word += i
    return word

if __name__ == "__main__":
    print(no_vowels("this is an example"))