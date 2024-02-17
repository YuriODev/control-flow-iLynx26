def test_function(x1, y1, x2, y2):
    dist1 = abs(x1)**2 + abs(y1)**2
    dist2 = abs(x2)**2 + abs(y2)**2
    print(dist1, dist2)
    if dist1 > dist2:
        return "A is further from the origin."
    elif dist1 < dist2:
        return "B is further from the origin."
    else:
        return "A and B are at the same distance from the origin."
 
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(test_function(x1, y1, x2, y2))