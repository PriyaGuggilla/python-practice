import random 

while True:

  secret = random.randint(1,100)
  attempts = 0
  guesses = []

  while attempts < 5 :
    try:
      guess = int(input("Enter a number: "))
    except:
      print("Please enter a valid number!")
      continue
  
    guesses.append(guess)
    attempts +=1
   
    if guess < secret:
      print("Too Low")
    elif guess > secret:
      print("Too High")
    else:
      print("Correct!")
      print("Attempts=",attempts)
      print("The secret number was", secret)
      print("\nYour guesses:")
      for guess in guesses:
              print(guess)
      break
  if attempts == 5 and guess != secret:
      print("\nGame Over!")
      print("The secret number was", secret)

      print("\nYour guesses:")
      for g in guesses:
          print(g)
  play_again = input("\nDo you want to play again? (y/n): ")

  if play_again.lower() == "n":
          print("Thanks for playing!")
          break
