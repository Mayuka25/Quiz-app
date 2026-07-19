from questions import questions

def run_quiz():
    score = 0
    review = []

    print("=== Welcome to the Quiz App ===\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        correct = answer == q['answer']
        if correct:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")

        review.append((q['question'], answer, q['answer'], correct))

    total = len(questions)
    percentage = (score / total) * 100
    result = "Pass" if percentage >= 50 else "Fail"

    print("=== Quiz Finished ===")
    print(f"Score: {score}/{total} ({percentage:.1f}%) - {result}\n")

    print("=== Review ===")
    for question, user_ans, correct_ans, correct in review:
        status = "✅" if correct else "❌"
        print(f"Q: {question}")
        print(f"Your answer: {user_ans} | Correct answer: {correct_ans} {status}\n")

if __name__ == "__main__":
    run_quiz()