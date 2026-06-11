while True:

 score = 0
 questions = [
    "What is 5 + 5? ",
    "What is 10 - 3? ",
    "What is 6 * 2? ",
    "What is 15 / 3? ",
    "What is 8 + 4? "
]

 answers = [
    "10",
    "7",
    "12",
    "5",
    "12"
]

 for i in range(len(questions)):
    user_answer = input(questions[i])

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", answers[i])

 print("\nQuiz Finished!")
 print("Your Score =", score, "/", len(questions))

 play_again = input("\nDo you want to play again(y/n):")

 if play_again.lower() == "n":
    print("Thanks for playing!")
    break
