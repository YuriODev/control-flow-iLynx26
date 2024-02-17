def test_function(n):
    n3 = n%10
    n2 = n%100 // 10
    n1 = n//100
    if n1 + n3 < n2:
        return "<"
    elif n1 + n3 > n2:
        return ">"
    else:
        return "="
    
n = int(input())
print(test_function(n))