def test_function(string):
    number = int(string)
    digit_1 = number//1000
    digit_2 = number%1000//100
    digit_3 = number%100//10
    digit_4 = number%10
    new_string = ""
    if digit_1 % 2 == 0:
        new_string += "*"
    else:
        new_string += str(digit_1)

    if digit_2 % 2 == 0:
        new_string += "*"
    else:
        new_string += str(digit_2)
     
    if digit_3 % 2 == 0:
        new_string += "*"
    else:
        new_string += str(digit_3)
    
    if digit_4 % 2 == 0:
        new_string += "*"
    else:
        new_string += str(digit_4)

    print(new_string)
    return new_string

string = input()
print(test_function(string))