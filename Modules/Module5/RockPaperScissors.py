import random
def main(): 
    print("acho papi a jugar rock paper scissors?")
    RPS = ["Rock", "Paper", "Scissors"]
    play_again = "y"

    while play_again == "y": 
        playerinput = input("bro yo voy a escoger roca. whats your move: \n")
        computerinput = random.choice(RPS)

        print(f"computer chose: {computerinput}")
        print(f"dumbass chose: {playerinput}")

        if(playerinput == computerinput): 
            print("you tied. *insert png of troll face*")
        elif (playerinput == "Rock" and computerinput == "Paper"): 
            print("you lost. *insert png of troll face*")
        elif (playerinput == "Scissors" and computerinput == "Paper"):
            print("bro??? you won??? *insert png of a troll face*")
        elif (playerinput == "Paper" and computerinput == "Scissors"):
            print("you lose bro.")
        else: 
            print("wtf you win") 
        play_again = input('type "y" to play again. "n" to not play again: ')
main()
