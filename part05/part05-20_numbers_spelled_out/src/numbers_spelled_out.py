# Write your solution here

def dict_of_numbers():
    dict = {}
    t1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    t11 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    t100 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    for i in range(100):
        if i < 11:
            dict[i] = t1[i]
        i = 0
        for i in range(len(t11)):
            dict[i+11] = t11[i]
        for i in range(20,100):
            m = i//10
            if i % 10 == 0:
                dict[i] = f"{t100[m-2]}"
            else:
                k = i % 10
                dict[i] = f"{t100[m-2]}-{t1[k]}"
    
    return(dict)

if __name__ == "__main__":
    dict_of_numbers()