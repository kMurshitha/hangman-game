# Problem Set 2, hangman.py
# Name: MURSHITHA K
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print(type(wordlist))
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for index in range(len(secret_word)):
        if secret_word[index] not in letters_guessed:
            return False
            continue
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for word in secret_word:
        if word in letters_guessed:
            guessed_word += word
        else:
            guessed_word += "_ "
    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remaining_alphabet = string.ascii_lowercase
    for word in letters_guessed:
        remaining_alphabet = remaining_alphabet.replace(word, "")
    return remaining_alphabet


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print(
        "Welcome to the game Hangman! \nI am thinking of a word that is {} letters long.  \n You have 3 warnings left.\n-------------".format(
            len(secret_word)
        )
    )

    guesses = 6
    vowels = "aeiou"
    warnings = 3
    gameEnd = False
    while not gameEnd:
        print(
            "You have {} guesses left. \nAvailable letters: {} ".format(
                guesses, get_available_letters(letters_guessed)
            )
        )
        guesses_word = input("Please guess a letter:")
        if (
            guesses_word in string.ascii_lowercase
            or guesses_word in string.ascii_uppercase
        ):
            guesses_word = guesses_word.lower()

            if guesses_word in get_available_letters(letters_guessed):
                letters_guessed.append(guesses_word)

                if guesses_word in secret_word:
                    guessed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", guessed_word)
                else:
                    if guesses_word in vowels:
                        guesses -= 2
                        print(
                            "Oops! That letter is not in my word:",
                            get_guessed_word(secret_word, letters_guessed),
                        )
                    else:
                        print(
                            "Oops! That letter is not in my word:",
                            get_guessed_word(secret_word, letters_guessed),
                        )
                        guesses -= 1

            else:
                if warnings > 0:
                    warnings -= 1
                    print(
                        " Oops! You've already guessed that letter. You have",
                        warnings,
                        "warnings left:",
                        get_guessed_word(secret_word, letters_guessed),
                    )
                else:
                    guesses -= 1
                    print(
                        " Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",
                        get_guessed_word(secret_word, letters_guessed),
                    )

        else:
            if warnings > 0:
                warnings -= 1
                print(
                    " Oops! That is not a valid letter.  You have",
                    warnings,
                    "warnings left:",
                    get_guessed_word(secret_word, letters_guessed),
                )
            else:
                guesses -= 1
                print(
                    " Oops! That is not a valid letter. You have no warnings left so you lose one guess: ",
                    get_guessed_word(secret_word, letters_guessed),
                )
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print(
                "Congratulations, you won! \nYour total score for this game is:",
                guesses * len(set(secret_word)),
            )
            gameEnd = True
        elif guesses <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            gameEnd = True


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(guessed_word, other_word):
    """
    guessed_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of guessed_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and guessed_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = False
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    guessed_word = guessed_word.replace(" ", "")
    if len(guessed_word) == len(other_word):
        for index in range(len(guessed_word)):
            if guessed_word[index] == "_" or guessed_word[index] == other_word[index]:
                result = True
                continue
            else:
                result = False
                break
    return result


def show_possible_matches(guessed_word):
    """
    guessed_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches guessed_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    hint = ""
    for other_word in wordlist:
        if match_with_gaps(guessed_word, other_word):
            hint += other_word + " "
    print(hint)


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(
        "Welcome to the game Hangman! \nI am thinking of a word that is {} letters long.  \n You have 3 warnings left.\n-------------".format(
            len(secret_word)
        )
    )

    guesses = 6
    vowels = "aeiou"
    warnings = 3
    gameEnd = False
    while not gameEnd:
        print(
            "You have {} guesses left. \nAvailable letters: {} ".format(
                guesses, get_available_letters(letters_guessed)
            )
        )
        if guesses < 3:
            print("Now you can use hints. Enter * for hints")
        guesses_word = input("Please guess a letter:")
        if (
            guesses_word in string.ascii_lowercase
            or guesses_word in string.ascii_uppercase
        ):
            guesses_word = guesses_word.lower()

            if guesses_word in get_available_letters(letters_guessed):
                letters_guessed.append(guesses_word)

                if guesses_word in secret_word:
                    guessed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", guessed_word)
                else:
                    if guesses_word in vowels:
                        guesses -= 2
                        print(
                            "Oops! That letter is not in my word:",
                            get_guessed_word(secret_word, letters_guessed),
                        )
                    else:
                        print(
                            "Oops! That letter is not in my word:",
                            get_guessed_word(secret_word, letters_guessed),
                        )
                        guesses -= 1

            else:
                if warnings > 0:
                    warnings -= 1
                    print(
                        " Oops! You've already guessed that letter. You have",
                        warnings,
                        "warnings left:",
                        get_guessed_word(secret_word, letters_guessed),
                    )
                else:
                    guesses -= 1
                    print(
                        " Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",
                        get_guessed_word(secret_word, letters_guessed),
                    )

        else:
            if guesses < 3:
                if guesses_word == "*":
                    print("\n")
                    guessed_word = get_guessed_word(secret_word, letters_guessed)
                    show_possible_matches(guessed_word)
                    print("\n")
            elif warnings > 0:
                warnings -= 1
                print(
                    " Oops! That is not a valid letter.  You have",
                    warnings,
                    "warnings left:",
                    get_guessed_word(secret_word, letters_guessed),
                )
            else:
                guesses -= 1
                print(
                    " Oops! That is not a valid letter. You have no warnings left so you lose one guess: ",
                    get_guessed_word(secret_word, letters_guessed),
                )
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print(
                "Congratulations, you won! \nYour total score for this game is:",
                guesses * len(set(secret_word)),
            )
            gameEnd = True
        elif guesses <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            gameEnd = True


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)

    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    letters_guessed = []
    secret_word = choose_word(wordlist)
    # hangman(secret_word)
    hangman_with_hints(secret_word)
