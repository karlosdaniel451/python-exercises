def function4(number: int | float) -> str:
    if (number > 0):
        return 'P'
    else:
        return 'N'


print(function4(-1))

print(function4(0))

print(function4(1))