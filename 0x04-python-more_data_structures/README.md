This is a README file of 0x04 directory

*** other methode of -- 1-search_replace.py -- : ***
    #!/usr/bin/python3
    def search_replace(my_list, search, replace):
        new_list = []
        for element in my_list:
            if element == search:
                element = replace
            new_list.append(element)
        return new_list

*** other methode of -- 3-common_elements.py -- : ***
    common_set = set()
    for element_1 in set_1:
        for element_2 in set_2:
            if element_1 == element_2:
                common_set.add(element_1)
    return common_set