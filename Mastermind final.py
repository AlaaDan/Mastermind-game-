import random
secret_numbers = random.randrange(1000, 9999)
secret_numbers = str(secret_numbers)
def game():
    tries_number = 0
    print('''Welcome to Mastermind Game
You need to guess the combination of a number which contains 4 digests.
If you guess one of the numbers correctly, but it's not on the right place the program will notify you.''')
    print('The secret number is', secret_numbers)
    wrong_place = 0
    guess = ['-', '-', '-', '-']
    input_number = 0

    while True:
        player = input('Enter your guess: ')
        for i in player:# to sum how many digests the user entered.
            input_number += 1
        if input_number == 4:
            if player == secret_numbers and tries_number == 0:
                print('WOW in just one try. YOU ARE MASTERMIND')
                break
            else:
                tries_number +=1
                for digests in range(0, 4):
                    if player[digests] in secret_numbers and player[digests] != secret_numbers[digests]:
                        wrong_place += 1
                    if player[digests] == secret_numbers[digests]:
                        guess[digests] = player[digests]
                print('you have', wrong_place, 'correct but not in the right place, try harder!')
                print('You gussed', guess)
                #print('tries', tries_number)
                wrong_place = 0
                input_number = 0
            if player == secret_numbers and tries_number > 0:
                print('Nicely done, It took you', tries_number, 'tries to guess the number')
                break
        else:
            print('Wrong input! Enter 4 digests')
            input_number =0


game()