def count(string: str, letter: str) -> int:
    result = 0
    for i in string:
        if i == letter:
            result += 1

    return result


print(count(string='aeiou', letter='a'))
print(count(string='aeiouaeiou', letter='a'))
print(count(string='asdf', letter='z'))
