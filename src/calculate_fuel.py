def calculate_fuel(distance):
    if distance <= 0:
        raise ValueError("Distance must be greater than 0")
    fuel = distance / 10
    return fuel
