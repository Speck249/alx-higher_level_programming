#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for ls in range(list_length):
        try:
            result = my_list_1[ls] / my_list_2[ls]
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            my_list_3.append(result)
    return my_list_3
