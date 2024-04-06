def delete_question():
    while True:
        try:
            index = int(input("Enter the index of the question to delete: "))
            if index > 0 and index <= len(quiz_operations.quiz_data):
                break
            else:
                print("Invalid question index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

    try:
        quiz_operations.delete_question(index)
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Returning to the main menu.")
