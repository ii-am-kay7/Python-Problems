from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)

    return mylist

def player_guess():
    guess = " "

    while guess not in ['0','1','2']:
     guess = input("Pick number 1,2 or 0: ")

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == "o":
        print("You win!")
    else:
       print("wrong guess!")
       print(mylist)


mylist = [' ','o',' ']

mixed_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mixed_list,guess)
