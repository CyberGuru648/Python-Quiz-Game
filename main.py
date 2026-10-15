
# Python Quiz Game

score = 0

question = {
    "Category": "Python",
    "Question": "Which keyword defines a function?",
    "Options": ["def", "loop", "fun", "if"],
    "Correct": 0
}

question2 = {
    "Category": "Python",
    "Question": "Which data type stores multiple items in order?",
    "Options": ["int", "list", "float", "bool"],
    "Correct": 1
}

questions = [question, question2]

print("=" * 35)
print("       PYTHON QUIZ GAME")
print("=" * 35)
print("Instructions:")
print("- Choose the correct option (1-4).")
print("- Each correct answer earns 1 point.")
print("- Invalid choices will be rejected.")
print("=" * 35)

for q in questions:
    print("\nCategory:", q["Category"])
    print("\nQuestion:", q["Question"])

    for i in range(len(q["Options"])):
        print(f"{i + 1}. {q['Options'][i]}")

    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))

            if 1 <= answer <= len(q["Options"]):
                break
            else:
                print("Invalid choice! Enter a number from 1 to 4.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    if answer - 1 == q["Correct"]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect!")
        print("Correct answer:", q["Options"][q["Correct"]])

print("\n" + "=" * 35)
print("          QUIZ RESULTS")
print("=" * 35)
print(f"Your score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent work!")
elif score > 0:
    print("Good job! Keep learning.")
else:
    print("Keep practicing. You will improve!")

print("=" * 35)
