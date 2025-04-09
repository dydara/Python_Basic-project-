# 📚 Simple Quiz Game

def run_quiz():
    score = 0

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Berlin", "C. Rome", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 12", "C. 13", "D. 14"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "C"
        },
        {
            "question": "What language are we coding in?",
            "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
            "answer": "B"
        }
    ]

    print("\n🎮 Welcome to the Quiz Game!")
    print("Type A, B, C, or D to answer.\n")

    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"🏁 Quiz Over! Your final score: {score}/{len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
