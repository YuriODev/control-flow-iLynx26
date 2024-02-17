def test_function(n):
    if n == 0:
        return("Green")
    elif 0 < n < 11:
        return "Red" if n % 2 else "Black"
    elif 10 < n < 19:
        return "Black" if n % 2 else "Red"
    elif 18 < n < 29:
        return "Red" if n % 2 else "Black"
    elif 28 < n < 37:
        return "Black" if n % 2 else "Red"
    else:
        return "The bet will not play!"

n = int(input())
print(test_function(n))