import random

def get_random_word():
    words = ["stockholm", "göteborg", "malmö", "örebro", "uppsala", "karlstad", "linköping", "umeå"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6


    print("Välkommen till Hangman, temat är svenska städer!")
    print(display_word(word, guessed_letters))
    
    while attempts > 0:
        guess = input("Gissa en bokstav eller hela ordet ;) : ").lower()
        
        if word == guess:
            print("Grattis! Du vann!")
            print(f"Du gissade hela ordet '{word}'.")
            print("vill du fortsätta? (y) om ja")
            answer = input().lower()
            if answer == "y":
                hangman()
            break
        
        if len(guess) != 1 or not guess.isalpha():
            print("Felaktig input. Ange en bokstav.")
            continue
        
        if guess in guessed_letters:
            print("Du har redan gissat på den bokstaven.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Bra gissat!")
        else:
            attempts -= 1
            print(f"Fel! Du har {attempts} försök kvar.")
        
        current_display = display_word(word, guessed_letters)
        print(current_display)
        
        if "_" not in current_display:
            print("Grattis! Du vann!")
            print(f"Ordet var '{word}'.")
            print("vill du fortsätta? (y) om ja")
            answer = input().lower()
            if answer == "y":
                hangman()
            break
    else:
        print(f"Du förlorade! Ordet var '{word}'.")
        print("vill du fortsätta? (y) om ja")
        answer = input().lower()
        if answer == "y":
            hangman()
        
hangman()