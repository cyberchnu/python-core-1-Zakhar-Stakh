def int_within_bounds(number, lower_bound, upper_bound):
    if isinstance(number, int) and lower_bound <= number < upper_bound:
        return True
    else:
        return False
