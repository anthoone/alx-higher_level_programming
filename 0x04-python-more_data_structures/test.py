#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates, then sum the set
    return sum(set(my_list))
my_list = [1, 2, 3, 1, 4, 2, 5]
print(uniq_add(my_list))