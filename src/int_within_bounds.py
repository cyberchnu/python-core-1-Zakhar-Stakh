def int_within_bounds(number, lower_bound, upper_bound):
  # Type your code
  if number >= lower_bound and number < upper_bound and type(number) == int:
   return True
  elif number < lower_bound or number >= upper_bound or type(number) == float:
    return False
