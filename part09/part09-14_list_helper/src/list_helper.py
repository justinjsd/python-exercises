# WRITE YOUR SOLUTION HERE:

class ListHelper:

    # Function to get the frequency of the elements of the list
    @staticmethod
    def frequency(my_list: list):
        frequency = {}

        for num in my_list:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        return frequency

    @classmethod   
    def greatest_frequency(cls, my_list: list) -> int:
        freq_dictionary = cls.frequency(my_list)
        
        most_frequent = max(freq_dictionary, key=freq_dictionary.get)

        return most_frequent

    @classmethod   
    def doubles(cls, my_list: list):
        times = 0
        freq_dictionary = cls.frequency(my_list)
        
        for value in freq_dictionary.values():
            if value >= 2:
                times += 1

        return times

if __name__ == "__main__":

    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]

    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))