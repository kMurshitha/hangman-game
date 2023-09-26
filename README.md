# Hangman Game

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Advanced Features](#advanced-features)
  - [Using Hints](#using-hints)

## Introduction

The Hangman Game is a classic word-guessing game where you try to guess a secret word letter by letter. With this Python-based Hangman Game, you can challenge yourself to solve words from a word list or play with friends. It's a fun and educational way to expand your vocabulary and test your word-guessing skills.

Key features of the Hangman Game include:

- **Random Word Selection**: The game selects a secret word at random from a predefined word list.
- **Interactive Gameplay**: You can guess letters one by one and receive feedback on whether your guess is correct.
- **Limited Guesses**: You have a limited number of guesses to complete the word. Don't run out of guesses!
- **Customizable Word List**: You can update the word list to include words of your choice or specific themes.
- **Hints (Advanced)**: For an extra challenge, you can use hints to discover words that match your current progress.

## Features

- Random word selection from a word list.
- Interactive letter guessing.
- Limited guesses for added challenge.
- Customizable word list.
- Hints for finding possible word matches (advanced feature).

## Getting Started

### Prerequisites

Before you can play the Hangman Game, ensure you have the following prerequisites:

- Python 3.x installed on your computer.

### Installation

1. Clone the Hangman Game repository to your local machine:

   ```shell
   git clone https://github.com/kMurshitha/hangman-game.git
   ```

2. Navigate to the project directory:

   ```shell
   cd hangman-game
   ```

3. Open the `words.txt` file and replace the default word list with your own words or themes. Each word should be on a separate line.

4. Run the game by executing the Python script:

   ```shell
   python hangman.py
   ```

The game should now start, and you can begin playing!

## How to Play

- The Hangman Game selects a secret word at random from the word list.
- You have a limited number of guesses to complete the word. By default, you start with 6 guesses.
- Before each round, the game displays the number of guesses left and the letters that you haven't guessed yet.
- Guess a letter by entering it via the keyboard.
- The game will provide immediate feedback on whether your guess is correct.
- After each guess, the game shows you the partially guessed word so far.
- Continue guessing letters until you complete the word or run out of guesses.

## Advanced Features

### Using Hints

- If you're stuck and need some help, you can use the hint feature.
- When you have fewer than 3 guesses left, you can enter `*` as a guess to request hints.
- The game will provide you with a list of words from the word list that match your current progress.
- Use this feature wisely, as it will consume one of your remaining guesses.

Enjoy playing the Hangman Game! Challenge yourself to guess words and have fun expanding your vocabulary. If you have any questions, encounter issues, or would like to contribute, please don't hesitate to get in touch with us. Happy guessing!
