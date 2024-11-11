# write your solution here
import difflib

def put_file_lines_in_list(file_name):
    with open(file_name) as file:
        file_as_list = []
        for line in file:
            line = line.replace('\n', '')
            file_as_list.append(line)
    return file_as_list

def main():
    text = input('Write text: ')
    text_list = text.split(' ')
    all_words = put_file_lines_in_list('wordlist.txt')
    for index, word in enumerate(all_words):
        all_words[index] = word.lower()
    output = ''
    wrongs = []
    for text in text_list:
        if text.lower() in all_words:
            output += text
        else:
            output += '*' + text + '*'
            wrongs.append(text)
        output += ' '
    print(output)
    print("suggestions: ")
    for wrong in wrongs: 
        print(f"{wrong}: ", end="")
        matches = difflib.get_close_matches(wrong, all_words)
        for match in matches:
            print(f"{match}, ", end="")
        print()

main()