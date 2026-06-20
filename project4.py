def run_quiz():
    score = 0
    total_questions = 3

    print("--- Welcome to the General Knowledge Quiz! ---")

    # Question 1
    q1 = input("1. What is the capital of France? ")
    if q1.lower() == "paris":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer was Paris.")

    # Question 2
    q2 = input("2. What is 5 + 7? ")
    if q2 == "12":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer was 12.")

    # Question 3
    q3 = input("3. Which planet is known as the Red Planet? ")
    if q3.lower() == "mars":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer was Mars.")

    # Final Score
    print("\n---------------------------")
    print(f"Quiz Complete! Your final score is: {score}/{total_questions}")
    print("---------------------------")

# Run the game
run_quiz()
