from pytest import mark

from src.fizzbuzz import fizzbuzz


@mark.fizzbuzz
@mark.parametrize(
    'multiple_of_only_3',
    [i for i in range(0, 100, 3) if i % 5 != 0]
)
def test_fizzbuzz_should_return_fizz(multiple_of_only_3: int):
    assert fizzbuzz(multiple_of_only_3) == 'fizz'


@mark.fizzbuzz
@mark.parametrize(
    'multiple_of_only_5',
    [i for i in range(0, 100, 5) if i % 3 != 0]
)
def test_fizzbuzz_should_return_buzz(multiple_of_only_5: int):
    assert fizzbuzz(multiple_of_only_5) == 'buzz'


@mark.fizzbuzz
@mark.parametrize(
    'multiple_of_both_3_and_5',
    [i for i in range(0, 100, 3) if i % 5 == 0]
)
def test_fizzbuzz_should_return_fizzbuzz(multiple_of_both_3_and_5: int):
    assert fizzbuzz(multiple_of_both_3_and_5) == 'fizzbuzz'


@mark.fizzbuzz
@mark.parametrize(
    'neither_multiple_of_3_nor_5',
    [i for i in range(0, 100) if i % 3 != 0 and i % 5 != 0]
)
def test_fizzbuzz_should_return_None(neither_multiple_of_3_nor_5: int):
    assert fizzbuzz(neither_multiple_of_3_nor_5) == None


@mark.fizzbuzz
def test_when_fizzbuzz_receives_multiple_of_only_3_then_should_return_fizz():
    assert fizzbuzz(6) == 'fizz'


@mark.fizzbuzz
def test_when_fizzbuzz_receives_multiple_of_only_5_then_should_return_buzz():
    assert fizzbuzz(10) == 'buzz'


@mark.fizzbuzz
def test_when_fizzbuzz_receives_multiple_of_both_3_and_5_then_should_return_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'


@mark.fizzbuzz
def test_when_fizzbuzz_do_not_receive_multiple_of_3_or_5_then_should_return_None():
    assert fizzbuzz(4) == None

