def test_function(grade):
    if 0 < grade < 4:
        return("initial level")
    elif 3 < grade < 7:
        return("average level")
    elif 6 < grade < 10:
        return("sufficient level")
    elif 9 < grade < 13:
        return("high level")
    else:
        return("level is absent")
    
grade = int(input())
print(test_function(grade))