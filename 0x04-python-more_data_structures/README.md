This is a README file of 0x04 directory

other methode of -- 1-search_replace.py -- : 
    #!/usr/bin/python3
    def search_replace(my_list, search, replace):
        new_list = []
        for element in my_list:
            if element == search:
                element = replace
            new_list.append(element)
        return new_list