def test_function(x1, x2, x3, y1, y2, y3):
    dist1 = abs(x1 - x2)**2 + abs(y1 - y2)**2
    dist2 = abs(x1 - x3)**2 + abs(y1 - y3)**2
    dist3 = abs(x2 - x3)**2 + abs(y2 - y3)**2
    # print(dist1, dist2, dist3)
    if dist1 == dist2 == dist3:
        return "No"
    elif (dist1 + dist2 == dist3) or (dist1 + dist3 == dist2) or (dist2 + dist3 == dist1):
        return "Yes"
    else: 
        return "No"

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

print(test_function(x1, x2, x3, y1, y2, y3))