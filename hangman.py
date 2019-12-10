import random
wordl = ["cat", "aardvark", "pig", "aligator", "walrus", "otter"]
rand = random.randint(0,5)
words = wordl[rand]
def hangman():
    wordl = ["cat", "aardvark", "pig", "aligator", "walrus", "otter"]
    rand = random.randint(0,5)
    word = wordl[rand]
    wrong = 0
    stages =["",
             "__________      ",
             "|               ",
             "|         |     ",
             "|         O     ",
             "|        /|\    ",
             "|        / \    ",
             "|               "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = ("Guess a letter. ")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind]= "$"

        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You Lose! it was {}.".format(word))


hangman()




        

