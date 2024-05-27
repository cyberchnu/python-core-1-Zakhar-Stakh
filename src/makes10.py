def makes10(a, b):
    if a + b == 10 or a == 10 or b == 10:
        if isinstance(a, int) and isinstance(b, int):
            return True
    return False
