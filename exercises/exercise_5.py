def test_function(a, b, c):

    if a == b == 0:
        return "No roots."
    if a == 0:
        x = -c / b
        return str(x)
    elif b == 0:
        x = (-c / a) ** 0.5
        return str(x)
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return "No roots."
        x1 = (b + d) / 2 /a
        x2 = (b - d) / 2 /a
        return f"{x1} and {x2}"

a = float(input())
b = float(input())
c = float(input())

print(test_function(a, b, c))