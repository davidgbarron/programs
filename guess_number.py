import random

class Game:
    def __init__(self):
        r = random.randint(1,11)
        tries = ["3","2","1"]
        #print(r)
        
        for number in tries:
            print(guess)
            #print("you have {} tries remaining.".format(i))
            sel = input("you have {} tries remaining:".format(number))
            sel = int(sel)
            
            
            if sel == r:
                print(s)
                print(win)
                restart = input(replay)
                if restart == "y":
                    Game()
                else:
                    print(s)
                    print(bye)
                    return None
            else:
                print(wrong)
                print(s)
                
        else:
            print(s)
            print(lose + ", the correct number was {}.".format(r))
            restart = input(replay)
            if restart == "y":
                Game()
            else:
                print(s)
                print(bye)
                return None
guess = ("please guess a number from 1 to 10.")
replay = ("would you like to play again? type y or n:")                               
bye = ("thank you for playing, goodbye.")
win = ("Correct! You Win!")
lose = ("sorry, you lose!")
wrong = ("incorrect guess!")
s = ("\n")
Game()
