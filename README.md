# Welcome to my Flashcards App!

This is a flashcard set designed for students learning foreign languages. It implements spaced repetition by placing the cards into boxes depending on if you know the answer or not. This tool will hopefully be helpful for students who are unable to buy learning applications, as this flashcards app is completely free to use!

# Intial Setup

- Install the [uv pacakge manager](docs.astral.sh/uv/getting-started/installation/)
- Run `uv sync`

# Running the web server
- Run `uv run py manage.py runserver`
- Open a browser to `localhost:8000`
- Start adding flashcards!

# How it works

On the landing page you will be able to add and edit your flashcards. Each flashcard has a question and an answer section. Once it is created, it is added to box 1.

Ex. Question: Manzana, Answer: Apple

You can add, delete, or edit any card from the "all cards" page at any time. Once every card has been moved to box 5, you have mastered the content and can move onto somthing new!

