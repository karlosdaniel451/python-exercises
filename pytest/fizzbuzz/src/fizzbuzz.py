def fizzbuzz(number: int) -> str | None:
    """
    Return 'fizz' if `number` is only multiple of 3, 'buzz' if `number`
    is only multiple of 5, 'fizzbuzz' if it is multiple of 3 and 5 or
    None otherwise.
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    
    if number % 3 == 0:
        return 'fizz'
    
    if number % 5 == 0:
        return 'buzz'
