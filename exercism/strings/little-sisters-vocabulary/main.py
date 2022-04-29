# For debugging purposes.
def main():
    print(adjective_to_verb(sentence='Look at the bright sky.', index=-2))
    print(adjective_to_verb(sentence='His expressions went dark.', index=-1))
    print(adjective_to_verb(sentence='The bread got hard after sitting out.', index=3))
    print(adjective_to_verb(sentence='The butter got soft in the sun.', index=3))
    print(adjective_to_verb(sentence='Her eyes were light blue.', index=-2))
    print(adjective_to_verb(sentence='The morning fog made everything damp with mist.', index=-3))
    print(adjective_to_verb(sentence='He cut the fence pickets short by mistake.', index=5))
    print(adjective_to_verb(sentence='Charles made weak crying noises.', index=2))
    print(adjective_to_verb(sentence='The black oil got on the white dog.', index=1))

"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f'un{word}'


def make_word_groups(vocab_words: list[str]):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    output = f'{prefix}'

    for word in vocab_words[1:]:
        output += f' :: {prefix}{word}'
    
    return output


def remove_suffix_ness(word: str):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    word_without_suffix = word.removesuffix('ness')

    if word_without_suffix[-1] == 'i':
        word_without_suffix = word_without_suffix[:-1] + 'y'

    return word_without_suffix


def adjective_to_verb(sentence: str, index: int):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    words_of_sentence = sentence.split()

    word_to_be_extracted = words_of_sentence[index]

    # In case it is the last word of sentence (ends with '.').
    if word_to_be_extracted[-1] == '.':
        word_to_be_extracted = word_to_be_extracted.rstrip('.')
    
    word_to_be_extracted = word_to_be_extracted + 'en'

    return word_to_be_extracted


if __name__ == '__main__':
    main()
    pass
