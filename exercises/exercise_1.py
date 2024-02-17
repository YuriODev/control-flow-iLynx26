def test_function(a, t):
    if a == t:
        return "Alex and Tatyana are of the same age."
    elif a > t:
        return "Alex is the eldest."
    elif t > a:
        return "Tatyana is the eldest."
    
a = int(input())
t = int(input())

print(test_function(a, t))

