def test_function(day, month, year):
    if day == 31:
        if month == 12:
            return f"1.1.{year+1}"
        else:
            return f"1.{month+1}.{year}"
    elif day == 30:
        return f"1.{month+1}.{year}"
    elif day == 29:
        return f"1.{month+1}.{year}"
    elif day == 28:
        return f"1.{month+1}.{year}"
    else:
        return(f"{day+1}.{month}.{year}")

day = int(input())
month = int(input())
year = int(input())

print(test_function(day, month, year))
