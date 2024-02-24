def test_function(day, month, year):
    if day == 1:
        if month == 1:
            return(f"31.12.{year-1}")
        elif month == 2 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11:
            return(f"31.{month-1}.{year}")
        elif month == 3:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                return(f"29.{month-1}.{year}")
            else:
                return(f"28.{month-1}.{year}")
        elif month == 5 or month == 7 or month == 10 or month == 11:
            return(f"30.{month-1}.{year}")
        else:
            return("Invalid month")
    else:
        return(f"{day-1}.{month}.{year}")

day = int(input())
month = int(input())
year = int(input())

print(test_function(day, month, year))
