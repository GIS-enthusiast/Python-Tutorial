from random import randint
import sys


def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
        else:
            print('hey bozo, I said 1~10')
            return False

    except TypeError:
        print('that was not a number')
        return TypeError


if __name__ == '__main__':
    # generate a number 1~10
    answer = randint(1, 10)

    # input from user?
    # check that input is a number 1~10
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            # if the function runs and returns True.., break out as you guessed the correct number.
            if (run_guess(guess, answer)):
                break

        except ValueError:
            print('please enter a number')
            continue
