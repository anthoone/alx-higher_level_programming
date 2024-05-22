#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
<<<<<<< HEAD
        return my_list
=======
        return my_list
>>>>>>> 05ee0616803e64bef85f137f5cf3056997130abe
