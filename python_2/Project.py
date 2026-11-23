# project 1 
# STEP 1: Show what this is about
game_title = "Guessing Game"
print(game_title)
print("Welcome! You must guess the correct words to win.")

max_attempts = 3

# --- Round 1 ---
word1 = "Cat"
hint1 = "It is a home pet"
game_won = False
print(f"\nHint: {hint1}")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")
    if guess.lower() == word1.lower():
        print("Correct!")
        game_won = True
        break
    else:
        print("Incorrect.")

if not game_won:
    print(f"The Answer was: {word1}")

print("Thank you so much for playing, now you are on to the hard question, Good Luck")

# --- Round 2 ---
word2 = "Stairs"
hint2 = "It goes up and down, but never moves, who am I?"
game_won = False
print(f"\nHint: {hint2}")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")
    if guess.lower() == word2.lower():
        print("Thank you so much for playing, you guessed it right!!")
        game_won = True
        break
    else:
        print("Incorrect.")

if not game_won:
    print(f"The Answer was: {word2}")

# --- Round 3 ---
word3 = "Elephant"
hint3 = "I am gray, I have two huge ears, who am I?"
game_won = False
print(f"\nHint: {hint3}")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")
    if guess.lower() == word3.lower():
        print("Thank you so much for playing, you guessed it right!!")
        game_won = True
        break
    else:
        print("Incorrect.")

if not game_won:
    print(f"The Answer was: {word3}")
    
# --- Round 4 ---
word4 = "Apple"
hint4 = "I am red sometimes, and green sometimes too, who am I?"
game_won = False
print(f"\nHint: {hint4}")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")
    if guess.lower() == word4.lower():
        print("Thank you so much for playing, you guessed it right!!")
        game_won = True
        break
    else:
        print("Incorrect.")

if not game_won:
    print(f"The Answer was: {word4}")

# --- Round 5 ---
word5 = "Owl"
hint5 = "I stay awake all night, I can turn my head almost all the way around and I say Hoo, who am I?"
game_won = False
print(f"\nHint: {hint5}")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")
    if guess.lower() == word5.lower():
        print("Thank you so much for playing, you guessed it right!!")
        game_won = True
        break
    else:
        print("Incorrect.")

if not game_won:
    print(f"The Answer was: {word5}") 

# --- Round 6 ---
word6 = "Lion"
hint6 = "I have a big mane, I live in the savanna, and I am the king of the jungle, What am I?" 
game_won = False
print(f"\nHint: {hint6}")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")
    if guess.lower() == word6.lower():
        print("Thank you so much for playing, you guessed it right!!")
        game_won = True
        break
    else:
        print("Incorrect.")
              
if not game_won:
    print(f"The Answer was: {word6}") 

print("\nGame Over! Thanks for playing!")
print("Hello World\nI have come\n to warn you all\n that your time has come\n to get an A!")