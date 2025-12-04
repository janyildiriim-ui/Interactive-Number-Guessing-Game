import random

print("Welcome to the number guessing game")

while True:
 secret   = random.randint(1,100)
 tries = 1
    # small spacing issue above

 print("I picked a number between 1 and 100")

 guess=0

 while( guess != secret ):
     guess = int(input("Make a guess: "))

     if guess < secret:
        print("Try something bigger")
     elif (guess > secret):
            print("Maybe try something smaller")
     else:
        print("Nice you got it. Tries:", tries)
        break

     tries = tries+1 

 again = input("Play again? (Y): ")
 if(again!="Y"):
        print("Closing the game...")
        break

print("Game over")