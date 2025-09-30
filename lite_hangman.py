import nltk
from nltk.corpus import words
import random
def check_letter(letter,cword,display):
    for i in range (len(cword)):
        if letter.lower()==cword[i].lower():
            display[i]=letter

    print(" ".join(display))
    return display


word_store =words.words()

computer_word=random.choice(word_store)
computer_word_list=list(computer_word)

word_length=len(computer_word)
display=["_"]*word_length
wrong=0
guesses=0
lives=6
print("Welcome to Word Guess!")
print(f"The word has {word_length} letters: ")
while wrong <6:
    guesses+=1
    display_checker="".join(display)
    display=check_letter(input("Guess a letter: "),computer_word,display)
    if display_checker=="".join(display):
        wrong+=1
        lives-=1
        print(f"Not in the word.{lives } lives remaining...")

    else:
        print(f"Good Guess!{lives } lives remaining...")
    if "".join(display)==computer_word:
        print(f"Congratulations, you did it in {guesses} guesses!")
        break

print(f"The word was: {computer_word}")#read on this method