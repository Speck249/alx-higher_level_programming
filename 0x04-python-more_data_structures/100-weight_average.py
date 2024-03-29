#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        numerator = [x * y for x, y in my_list[0:]]
        denominator = [num[1] for num in my_list]
        weighted_avg = sum(numerator) / sum(denominator)
        return weighted_avg
    return 0
