from math import floor


# For debuggin purposes.
def main():
    print(get_rounds(27))
    print(concatenate_rounds(rounds_1=[27, 28, 29], rounds_2=[35, 36]))
    print(approx_average_is_average(hand=[1, 2, 3]))
    print(approx_average_is_average(hand=[2, 3, 4, 8, 8]))
    print(approx_average_is_average(hand=[1, 2, 3, 5, 9]))
    print(average_even_is_average_odd(hand=[1, 2, 3]))
    print(average_even_is_average_odd(hand=[1, 2, 3, 4]))


"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    median = hand[floor(len(hand) / 2)]

    # return (hand[0] + hand[-1]) / 2 == average or median == average
    return average in ((hand[0] + hand[-1]) / 2, median)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    sum_of_even_positions = 0
    number_of_even_positions = 0

    sum_of_odd_positions = 0
    number_of_odd_positions = 0

    for index, card in enumerate(hand):
        if index % 2 == 0:
            sum_of_even_positions += card
            number_of_even_positions += 1
        else:
            sum_of_odd_positions += card
            number_of_odd_positions += 1

    return sum_of_even_positions / number_of_even_positions == \
        sum_of_odd_positions / number_of_odd_positions


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    hand_with_double_jack = hand[:]

    if hand_with_double_jack[-1] == 11:
        hand_with_double_jack[-1] = 22

    return hand_with_double_jack


if __name__ == '__main__':
    # main()
    pass
