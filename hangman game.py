import random
from tkinter import Tk, Label, Entry, Button, StringVar, Frame
from collections import Counter, deque


someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon
 coconut watermelon cherry papaya berry peach lychee muskmelon fig'''.split()

# choose a random fruit
word = random.choice(someWords)
guessed_word = ['_'] * len(word)
guessed_letters = set()
letter_positions = {char: [i for i, c in enumerate(word) if c == char] for char in set(word)}
guess_history = deque(maxlen=10)
chances = len(word) + 2

def disable_game():
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

# updating the guessed letter
def update_display():
    display_var.set(' '.join(guessed_word))


def update_message(msg, color="black"):
    message_var.set(msg)
    message_label.config(fg=color)

# check guesses
def check_guess():
    global chances
    guess = guess_var.get().lower()
    guess_var.set('')

    if not guess.isalpha() or len(guess) != 1:
        update_message("Invalid input! Enter a single letter.", "red")
        return

    if guess in guessed_letters:
        update_message(f"You already guessed '{guess}'.", "orange")
        return

    guessed_letters.add(guess)
    guess_history.append(guess)

    if guess in letter_positions:
        for pos in letter_positions[guess]:
            guessed_word[pos] = guess
        update_display()

        if '_' not in guessed_word:
            update_message(f"Congratulations! You won! The word was '{word}'.", "green")
            reset_game_button.pack(pady=10)
            disable_game()
    else:
        chances -= 1
        chances_var.set(f"Chances Left: {chances}")

        if chances == 0:
            update_message(f"Game Over! The word was '{word}'.", "red")
            reset_game_button.pack(pady=10)
            disable_game()
        else:
            update_message(f"'{guess}' is not in the word. Try again!", "blue")

# Reset the game
def reset_game():
    global word, guessed_word, guessed_letters, letter_positions, guess_history, chances
    word = random.choice(someWords)
    guessed_word = ['_'] * len(word)
    guessed_letters = set()
    letter_positions = {char: [i for i, c in enumerate(word) if c == char] for char in set(word)}
    guess_history.clear()
    chances = len(word) + 2
    update_display()
    chances_var.set(f"Chances Left: {chances}")
    update_message("Start guessing the new word!", "black")
    reset_game_button.pack_forget()
    guess_entry.config(state="normal")
    guess_button.config(state="normal")

# UI
root = Tk()
root.title("Hangman Game")
root.geometry("500x450")
root.configure(bg="#f5f5f5")


Label(root, text="Hangman Game", font=("Comic Sans MS", 24, "bold"), fg="#333", bg="#f5f5f5").pack(pady=10)

# frame for guessed word display
guess_frame = Frame(root, bg="#f5f5f5")
guess_frame.pack(pady=20)
Label(guess_frame, text="Guess the fruit:", font=("Arial", 18), bg="#f5f5f5", fg="#555").grid(row=0, column=0, padx=10)
display_var = StringVar()
display_var.set(' '.join(guessed_word))
Label(guess_frame, textvariable=display_var, font=("Arial", 18), bg="#f5f5f5", fg="#0077cc").grid(row=0, column=1)

# input and submit button
input_frame = Frame(root, bg="#f5f5f5")
input_frame.pack(pady=20)
Label(input_frame, text="Enter a letter:", font=("Arial", 14), bg="#f5f5f5", fg="#555").grid(row=0, column=0, padx=10)
guess_var = StringVar()
guess_entry = Entry(input_frame, textvariable=guess_var, font=("Arial", 14), width=5, justify='center')
guess_entry.grid(row=0, column=1, padx=10)
guess_button = Button(input_frame, text="Guess", command=check_guess, font=("Arial", 14), bg="#0077cc", fg="white", relief="flat", cursor="hand2")
guess_button.grid(row=0, column=2, padx=10)

# chances display
chances_var = StringVar()
chances_var.set(f"Chances Left: {chances}")
Label(root, textvariable=chances_var, font=("Arial", 14), bg="#f5f5f5", fg="#555").pack(pady=10)

# displaying message
message_var = StringVar()
message_var.set("Start guessing the word!")
message_label = Label(root, textvariable=message_var, font=("Arial", 12), bg="#f5f5f5", fg="black")
message_label.pack(pady=10)

# reset game button
reset_game_button = Button(root, text="Play Again", command=reset_game, font=("Arial", 14), bg="#28a745", fg="white", relief="flat", cursor="hand2")


Label(root, text="Can you guess the word before you run out of chances?", font=("Arial", 12), bg="#f5f5f5", fg="#888").pack(side="bottom", pady=10)

# starting of program 
root.mainloop()
