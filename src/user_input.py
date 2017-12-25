def get_user_sign():
    """
    Gets the sign from user input.
    :return:
    """

    artist = input("Enter the sign for searching: ")

    return artist


def get_user_song(check_func):
    """
    Gets the song from user input.
    :param check_func: the function that will be used to check user input
    :return:
    """

    hint = "Enter the song number: "

    song_number = input(hint)

    while not check_func(song_number):
        song_number = input(hint)

    return song_number


def cast_to_int(text):
    """
    Returns int from text or False if cast is not possible.
    :param text: user input
    :return:
    """
    num_int = False

    try:
        num_int = int(text)
    except ValueError:
        pass

    return num_int


def check_user_int(user_input, max_value):
    """
    Returns True if user_input is int in [1, max_value] else False
    :param user_input: user input
    :param max_value: the maximum value
    :return:
    """

    result = False

    if type(user_input) == int:
        if 1 <= user_input <= max_value:
            result = True

    return result


def get_user_saving_details():
    """
    Asks user save the chords or not.
    If answer Yes, ask the local directory name for saving.
    :return:
    """

    hint = "Do you want to save chords? (y/n) "
    possible_answers = ["y", "n"]

    answer = input(hint)

    while answer not in possible_answers:
        answer = input(hint)

    if answer == "y":
        directory = input("Enter the directory path to save: ")

        return directory

