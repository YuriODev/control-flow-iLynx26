def test_function(n1, n2):
    return str(n2) in str(n1)

n1 = int(input())
n2 = int(input())

print(test_function(n1, n2))