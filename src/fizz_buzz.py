def fizz_buzz(param):
  #Type your code here
  if param % 3 == 0 and % 5 == 0:
      result = "Fizz"
  elif param % 5 == 0:
      result = "Buzz"
  elif param % 3 == 0:
      result = "FizzBuzz"
  else: result = str(param)
  return (result)
