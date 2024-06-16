a = "aabcdee"

def addFreq(a):

    freq_dict = {}
    for char in a:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

print(addFreq(a))
