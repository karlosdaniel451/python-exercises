# Yes, it turned out to be an exercise about dictionaries, but it was
# on the section about lists and list methods, so anyways...

colors_code = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}


def color_code(color: str) -> int:
    return colors_code[color]


def colors() -> list[str]:
    return list(colors_code.keys())
