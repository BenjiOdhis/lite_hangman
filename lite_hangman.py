import nltk#add hints,hint counter...hints cost you lives
from nltk.corpus import words
import random

def check_letter(letter,cword,display,guessedset):
    alphabets=set("abcdefghijklmnopqrstuvwxyz")
    if letter in guessedset:
        print("You have already guessed that letter")
        
        invalid=1
    elif letter not in alphabets:
        print("Enter a letter in the alphabet")
        
        invalid=1
    else:
        for i in range (len(cword)):
         if letter.lower()==cword[i].lower():
            display[i]=letter
            guessedset.add(letter)
        else:
            guessedset.add(letter)
        
        invalid=0

        print(" ".join(display))
        print(guessedset)
    return display,invalid


word_store =words.words()

computer_word=random.choice(word_store)
computer_word_list=list(computer_word)

word_length=len(computer_word)
display=["_"]*word_length
wrong=0
guesses=0
lives=6
guessed_letters=set()


print("Welcome to Word Guess!")
print(f"The word has {word_length} letters: ")
while wrong <6:
    guesses+=1
    display_checker="".join(display)
    #tuple unpacking
    display,invalid=check_letter(input("Guess a letter: "),computer_word,display,guessed_letters)
    if display_checker=="".join(display):
        wrong=wrong+1-invalid
        lives=lives-1+invalid
        print(f"Not in the word.{lives } lives remaining...")

    else:
        print(f"Good Guess!{lives } lives remaining...")
    if "".join(display)==computer_word:
        print(f"Congratulations, you did it in {guesses} guesses!")
        break

print(f"The word was: {computer_word}")#read on this method