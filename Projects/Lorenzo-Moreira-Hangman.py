import random
word_list = ["guaynabo", "aguadilla", "utuado", "gurabo", "fajardo", "hormigueros", "mayaguez", "arecibo", "luquillo", "ponce"]
def get_word(word_list):
   word = random.choice(word_list)
   return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print("Theme: Pueblos de PR")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0: 
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess is guessed_letters:
                print ("You already tried" + guess)
            elif guess not in word: 
                print(guess + "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print ("Nice!" + guess + " was in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess] 
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already tried", guess, "!")
            elif guess != word: 
                print(guess, " isnt in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else: 
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("good job, you guessed the word !111")
    else:
        print("im sorry bro you have 0 tries. the word was " + word + ", try again")

def display_hangman(tries): 
    stages = [ """
                --------
                |   |
                |   O
                |  /|\\
                |   |
                |  / \\
                -
                """,
                """
                --------
                |   |
                |   O
                |  /|\\
                |   |
                |  /
                -
                """,
                """
                --------
                |   |
                |   O
                |  /|\\
                |   |
                |   
                -
                """,
                """
                --------
                |   |
                |   O
                |  /|
                |   |
                |   
                -
                """,
                """
                --------
                |   |
                |   O
                |   |
                |   |
                |   
                -
                """,
                """
                --------
                |   |
                |   O
                |   
                |   
                |  
                -
                """,
                """
                --------
                |   |
                |   
                |  
                |   
                |  
                -
                """,
                """
""" 
    ]
    return stages[tries]
def main():
    word = get_word(word_list)
    play(word)
    while input("again? (y/n) ").upper() == "Y":
        word = get_word(word_list)
        play(word)
if __name__ == "__main__":
    main()