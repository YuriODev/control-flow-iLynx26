def test_function(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Leap year."
    else:
        return "Ordinary year."

year = int(input())
print(test_function(year))