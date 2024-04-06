class QuizGame:
    def __init__(self):
        self.questions = []

    def add_question(self, question, answer):
        """Add a new question to the quiz"""
        self.questions.append({"question": question, "answer": answer})
        print("Question added successfully!")

    def view_questions(self):
        """View all questions in the quiz"""
        if not self.questions:
            print("No questions available.")
        else:
            print("Quiz Questions:")
            for idx, q in enumerate(self.questions, 1):
                print(f"{idx}. {q['question']}")

    def update_question(self, idx, new_question, new_answer):
        """Update an existing question"""
        if 1 <= idx <= len(self.questions):
            self.questions[idx - 1] = {"question": new_question, "answer": new_answer}
            print("Question updated successfully!")
        else:
            print("Invalid question index.")

    def delete_question(self, idx):
        """Delete an existing question"""
        if 1 <= idx <= len(self.questions):
            del self.questions[idx - 1]
            print("Question deleted successfully!")
        else:
            print("Invalid question index.")

    def start_game(self):
        """Start the quiz game"""
        if not self.questions:
            print("No questions available to start the game.")
            return

        print("Quiz Game Started!")
        score = 0
        for idx, q in enumerate(self.questions, 1):
            print(f"Question {idx}: {q['question']}")
            user_answer = input("Your Answer: ").strip().lower()
            if user_answer == q['answer'].lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        print(f"Game Over! Your Score: {score}/{len(self.questions)}")


def main():
    quiz = QuizGame()

    while True:
        print("\n===== Quiz Game Menu =====")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            quiz.add_question(question, answer)
        elif choice == '2':
            quiz.view_questions()
        elif choice == '3':
            idx = int(input("Enter the question index to delete: "))
            quiz.delete_question(idx)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
