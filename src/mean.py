def mean(number):
    sum = 0
    strnumber = str(number)
    for i in strnumber:
        sum += int(i)
    return sum / len(strnumber)
