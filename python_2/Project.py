#project 1 for semester 1
# STEP 1: Show what this is about
game_title = "Guessing Game"  
print(game_title)
print("Welcome! You must guess the correct words to win.")

# --- Round 1 ---
word1 = "Cat"  # str
hint1 = "It is a home pet"
max_attempts = 3 # int
game_won = False  # bool

print(f"Hint: {hint1}")

# Looping time for repeated steps
for attempt in range(1, max_attempts + 1):
  guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")

  # Decision-making 
  if guess.lower() == word1.lower():
    print("Correct!")
    game_won = True
    break
  else:
    print("Incorrect.")

if not game_won:
  print(f"The Answer was: {word1}")

print(
    "Thank you so much for playing, now you are on to the hard question, Good Luck")

# --- Round 2 ---
word2 = "Stairs" 
hint2 = "What goes up and down, but always remains in the same place?"
game_won = False

print(f"Hint: {hint2}")

for attempt in range(1, max_attempts + 1):
  guess = input(f"Enter your guess (Attempt {attempt}/{max_attempts}): ")

  if guess.lower() == word2.lower():
    print("Thank you so much you for playing, you guessed it right!!")
    game_won = True
    break
  else:
    print("Incorrect.")

if not game_won:
  print(f"The Answer was: {word2}")