def mean(number):
  # Type your code
  sum = 0
  strnumber = str(number)
  for i in strnumber:
    sum = sum + int(i)
    return sum /len(strnumber)

