# Write your function here
def over_nine_thousand(lst):
    sum1 = 0
    for number in lst:
        sum1 += number
        if sum1 > 9000:
            break
    return sum1


print(over_nine_thousand([8000, 900, 120, 5000]))
