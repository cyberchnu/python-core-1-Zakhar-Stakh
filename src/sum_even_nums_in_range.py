def sum_even_nums_in_range(start, stop):
    result = 0
    for i in range(start, stop + 1):
        if i % 2 == 0:
            result += i
    return result
