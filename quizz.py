# ============================================
# Python Quiz Application
# Built by: Kush
# ============================================

# --- QUESTIONS DATABASE ---
# Each question is a dictionary with:
# "question" = the question text
# "options"  = 4 choices (A, B, C, D)
# "answer"   = the correct letter

questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Process Unit", "B) Central Processing Unit", "C) Computer Personal Unit",
                    "D) Core Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a programming language?",
        "options": ["A) HTML", "B) Microsoft Word", "C) Python", "D) Google Chrome"],
        "answer": "C"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) **", "D) #"],
        "answer": "D"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A) Random Access Memory", "B) Read Access Module", "C) Run Application Memory",
                    "D) Random App Manager"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False in Python?",
        "options": ["A) String", "B) Integer", "C) Boolean", "D) Float"],
        "answer": "C"
    },
    {
        "question": "What is the correct way to print in Python?",
        "options": ["A) echo('Hello')", "B) print('Hello')", "C) console.log('Hello')", "D) display('Hello')"],
        "answer": "B"
    },
    {
        "question": "What does 'if' do in programming?",
        "options": ["A) Repeats code", "B) Stores a value", "C) Checks a condition", "D) Defines a function"],
        "answer": "C"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["A) List", "B) Dictionary", "C) Table", "D) Tuple"],
        "answer": "C"
    },
    {
        "question": "What does Git do?",
        "options": ["A) Runs Python code", "B) Tracks changes in your code", "C) Designs websites",
                    "D) Manages databases"],
        "answer": "B"
    },
    {
        "question": "What is an algorithm?",
        "options": ["A) A type of computer virus", "B) A step-by-step set of instructions to solve a problem",
                    "C) A programming language", "D) A type of database"],
        "answer": "B"
    }
]


# --- FUNCTIONS ---

def show_welcome():
    """Displays a welcome message when the quiz starts"""
    print("=" * 50)
    print("       WELCOME TO THE PYTHON QUIZ APP")
    print("=" * 50)
    print("Test your computer science knowledge!")
    print(f"Total Questions: {len(questions)}")
    print("=" * 50)
    print()


def ask_question(number, question_data):
    """
    Asks a single question and returns True if correct, False if wrong.

    number       = the question number (1, 2, 3...)
    question_data = the dictionary with question, options, and answer
    """
    print(f"Question {number}: {question_data['question']}")
    print()

    # Show all 4 options
    for option in question_data["options"]:
        print(f"   {option}")
    print()

    # Keep asking until user gives a valid answer (A, B, C, or D)
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            break  # valid answer, exit the loop
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    # Check if the answer is correct
    if user_answer == question_data["answer"]:
        print("Correct!\n")
        return True  # correct
    else:
        print(f"Wrong! The correct answer was: {question_data['answer']}\n")
        return False  # incorrect


def show_results(score, total):
    """Displays the final score and a performance message"""
    print("=" * 50)
    print("           QUIZ COMPLETE!")
    print("=" * 50)
    print(f"Your Score: {score} / {total}")

    # Calculate percentage
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")
    print()

    # Give feedback based on score
    if percentage == 100:
        print("Perfect score! Outstanding!")
    elif percentage >= 80:
        print("Great job! You know your stuff!")
    elif percentage >= 60:
        print("Good effort! Keep studying!")
    elif percentage >= 40:
        print("Not bad, but there's room to improve.")
    else:
        print("Keep practicing — you'll get there!")

    print("=" * 50)


def run_quiz():
    """Main function that runs the entire quiz"""
    show_welcome()

    score = 0  # tracks how many correct answers

    # Loop through every question
    for i, question_data in enumerate(questions):
        question_number = i + 1  # start from 1, not 0
        is_correct = ask_question(question_number, question_data)

        if is_correct:
            score += 1  # add 1 point for correct answer

        print("-" * 50)
        print()

    # Show final results
    show_results(score, len(questions))


# --- RUN THE PROGRAM ---
# This line makes sure the quiz only runs when you execute this file directly
if __name__ == "__main__":
    run_quiz()
