def find_string(string, sub_string):
    return(sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))

print(find_string("ABCDCDC", "CDC"))
