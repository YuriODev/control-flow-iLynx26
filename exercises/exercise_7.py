def test_function(a, b, arithm):
    if arithm == "+":
        return a + b
    elif arithm == "-":
        return a - b
    elif arithm == "/":
        if b == 0:
            return "Division by 0!"
        return a / b
    elif arithm == "*":	
        return a * b
    elif arithm == "pow":
        return a ** b
    elif arithm == "div":
        if b == 0:
            return "Division by 0!"
        return a // b
    elif arithm == "mod":
        return a % b
    else:
        return "Something isn't right"

a = float(input())
b = float(input())
arithm = str(input())

print(test_function(a, b, arithm))