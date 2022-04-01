# prints the string with enough leading spaces so that the last letter of the
# string is in column 70 of the display.
def right_justify(s: str) -> None:
    output = ' ' * (70 - len(s)) + s
    print(output)

right_justify('monty')
