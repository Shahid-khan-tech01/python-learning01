questions = (
    "How many pillars are there in Islam?",
    "What is the holy book of Islam?",
    "How many times do muslim pray daily?",
    "Who is the last prophet in Islam?",
    "In which month do muslim fast?"
)

options = (
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Bible", "B. bagwada", "C. Quran", "D. None"),
    ("A. 3", "B. 50", "C. 7", "D. 5"),
    ("A. Muhamad", "B. Yusuf", "C. Yunus", "D. Sulaiman"),
    ("A. Muhrram", "B. zawal", "C. Bakrid", "D. Ramadan")
)

answers = ("A", "C", "D", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("-------------------------")
print("         RESULTS")
print("-------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")