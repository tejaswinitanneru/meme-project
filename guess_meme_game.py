# guess_meme_game.py

import random
import pyjokes
import time
import os
from colorama import init, Fore, Back, Style
import pyfiglet

init(autoreset=True)

# List of memes
memes = [
    {"line": "Taggede ___", "answer": "le"},
    {"line": "Oka sari commit aithe ___", "answer": "na mata neene"},
    {"line": "Life ante ___ kaadu ra", "answer": "board exam"},
    {"line": "Nuvvu naku ___ ra", "answer": "chala istam"},
    {"line": "Ee roju ___ ledu", "answer": "santosham"},
    {"line": "They had us in the first half, not gonna ___", "answer": "lie"},
    {"line": "Why are you ___?", "answer": "running"},
]

# Create header with large single-line text
def print_title():
    banner = pyfiglet.figlet_format("GUESS THE MEME!", font="slant", width=200)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + banner)

# Final reaction with styled win/loss
def final_reaction(score):
    if score == 3:
        print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("YOU WON! 🥳", font="big"))
        print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "\n💣💥 BANG! You’re the MEME LEGEND! 💣💥")
        print(Fore.YELLOW + "🔥 Blasting Bloopers Unlocked 🔥")
        print("😂 'Kummestha... kannu musukoni navvesta' 😂")
        print("💥 'Ee meme lo logic undadhu, fun matram untadhi' 💥")
    else:
        print(Fore.RED + Style.BRIGHT + pyfiglet.figlet_format("YOU LOST 😢", font="big"))
        print(Fore.RED + Style.BRIGHT + "\n😢 Better luck next time! Keep practicing! 😢")
        roasts = [
            "😂 'Kummestha... kannu musukoni navvesta' 😂",
            "🙃 'Nee meme knowledge chala baagundhi ra babu!'",
            "👀 'Oka meme kooda correct cheyyalekapoyavaa?'"
        ]
        print(random.choice(roasts))
        print("\nHere’s a joke to cheer you up:")
        print(Fore.GREEN + pyjokes.get_joke())

# Game Logic
def play_game():
    print_title()
    score = 0

    selected_memes = random.sample(memes, 3)  # No repeat

    for i, meme in enumerate(selected_memes):
        print(Fore.LIGHTBLUE_EX + f"\nRound {i+1}")

        # Meme line in medium clear font
        question_text = pyfiglet.figlet_format(meme['line'], font="small", width=100)
        print(Fore.YELLOW + Style.BRIGHT + question_text)

        guess = input(Fore.WHITE + Style.BRIGHT + "Your guess: ").strip().lower()

        if guess == meme['answer'].lower():
            print(Fore.GREEN + "✅ Correct! You're a true memer!")
            score += 1
        else:
            print(Fore.RED + f"❌ Nope! Correct answer was: '{meme['answer']}'")
            print(Fore.MAGENTA + "😂 Bonus Joke: " + pyjokes.get_joke())

        time.sleep(1)

    # Final Score in big font
    result_font = pyfiglet.figlet_format(f"{score}/3", font="big")
    print(Fore.CYAN + "\nYour Score:\n" + result_font)

    final_reaction(score)

# Run the game
if __name__ == "__main__":
    play_game()