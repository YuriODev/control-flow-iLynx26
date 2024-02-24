def test_function(number):
    digit_1 = number//1000
    digit_2 = number%1000//100
    digit_3 = number%100//10
    digit_4 = number%10
    if digit_1 == digit_4 and digit_2 == digit_3:
        return True
    return False

number = int(input())
print(test_function(number))