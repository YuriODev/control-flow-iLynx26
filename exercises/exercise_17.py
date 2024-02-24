def test_function(ticket):
    digit_1 = ticket//100000
    digit_2 = ticket%100000//10000
    digit_3 = ticket%10000//1000
    digit_4 = ticket%1000//100
    digit_5 = ticket%100//10
    digit_6 = ticket%10

    if digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6:
        return("Happy")
    else:
        return("Ordinary")
    
ticket = int(input())
print(test_function(ticket))