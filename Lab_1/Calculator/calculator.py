# must perform n increments to the value m
def sum(m, n):
    if n == 0:
        return m
    iterations = abs(n)
    sign = 1 if n > 0 else -1  
    for _i in range(iterations):
        m += sign
    return m

# must subtract n from m until it gets to 0
def divide(m, n):
    if n == 0:
        return
    result = 0
    is_negative = m * n < 0
    m = abs(m)
    n = abs(n)
    while (m >= n):
        m -= n
        result += 1
    result = -result if is_negative else result