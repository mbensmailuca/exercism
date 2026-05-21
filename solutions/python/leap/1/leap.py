def leap_year(year):
    divisibleBy4 = year % 4 == 0
    divisibleBy100 = year % 100 == 0
    divisibleBy400 = year % 400 == 0
    return (divisibleBy4 and not divisibleBy100) or (divisibleBy100 and divisibleBy400)
    
