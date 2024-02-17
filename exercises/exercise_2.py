def test_function(age):
    if age <= 1:
        return("You are an infant.")
    elif age <= 13:
        return("You are a child.")
    elif age <= 20:
        return ("You are a teenager.")
    else:
        return ("You are an adult.")
    
age = int(input())
print(test_function(age))