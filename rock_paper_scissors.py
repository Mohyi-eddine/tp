"""
imported libraries
"""
import os
import random
import time

choices = ["paper", "rock", "scissors"]
GREEN = "\033[0;32m"


def choice_check(choice):
    """
    a function that returns a true value if ur choice is valid
    :param choice:
    :return:
    """
    return choice in choices


def choice_validation(player_choice):
    """
    a function that keeps asking for valid answer using choice check function
    :param player_choice:
    """
    loop = True
    while loop:
        if not choice_check(player_choice):
            print("not a valid option, expecting: ", choices[0], choices[1], "or", choices[2])
            player_choice = input()
        else:
            loop = False
    return player_choice


def winning_answer(choice1, choice2):
    """
   a function that  checks the winning combinations
    :param choice1:
    :param choice2:
    :return:
    """
    if choice1 in "rock" and choice2 in "scissors":
        return True

    if choice1 in "paper" and choice2 in "rock":
        return True

    if choice1 in "scissors" and choice2 in "paper":
        return True
    return False


def winning_player(win, loss):
    """
    a  function  that checks the winning player
    :param win:
    :param loss:
    """
    if win > loss:
        print("Sir maybe u didn't win all the fight but u surely won the war")
    elif win == loss:
        print("there is no winning side the fight will go on ")
    else:
        print("Sir maybe u won some fights but unfortunately skynet will concor the world")


def check_tie(choice1, choice2):
    """
a function that  checks if the combination is a tie
    :param choice1:
    :param choice2:
    :return:
    """
    return choice1 == choice2


def game_entrance():
    """
    a procedure that regroups all the entrance element of the game
    """
    os.system("cls")
    print(GREEN)
    print("### rock paper scissors game ###")


def game_size_input_validation(player_input):
    """
    a function that keeps asking for valid answer
    :param player_input:
    """
    loop = True
    while loop:
        try:
            if int(player_input):
                loop = False
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            player_input = input()
    return player_input


def retry():
    """
 a function that serves under certain conditions to play another game
    :rtype: object
    """
    player_choice = ''
    loop = True
    while loop:
        print("do u still have the courage to save world Y/N ?")
        player_choice = input()
        if player_choice.upper() == "Y" or player_choice.upper() == "N":
            loop = False

        else:
            print("Please choose between Y Or N : ")
    return player_choice.upper()


def main():
    """
   the main procedure that runs the game
    """
    resurrection = 'Y'
    while resurrection == 'Y':
        game_entrance()
        turns = 0
        win = 0
        loss = 0
        print("define how much  the fight against skynet goes on  :  ")
        turns_number = input()
        turns_number = game_size_input_validation(turns_number)
        while turns < int(turns_number):
            print(" type your choice: ")
            player_choice = input()
            player_choice = choice_validation(player_choice)
            print("you choose: ", player_choice)
            time.sleep(0.5)
            print("computer is thinking...")
            time.sleep(1)
            pc_choice = random.choice(choices)
            print("computer choose: ", pc_choice)
            print('\n')
            if check_tie(player_choice, pc_choice):
                os.system("cls")
                print("IT'S A TIE!!!")
                print('\n')
            if winning_answer(player_choice, pc_choice):
                os.system("cls")
                print(player_choice, " beats ", pc_choice)
                print("YOU WIN!!!")
                print('\n')
                win += 1
            # running = False
            elif (not winning_answer(player_choice, pc_choice) and
                  not check_tie(player_choice, pc_choice)):
                os.system("cls")
                print(pc_choice, " beats ", player_choice)
                print("YOU LOOSE!, ")
                print('\n')
                loss += 1
            turns += 1
        winning_player(win, loss)
        resurrection = retry()
    print("have a good day")


if __name__ == '__main__':
    main()
