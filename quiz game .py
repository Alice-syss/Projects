questions = [
    {
        "prompt": "What is the capital of france",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "What language is spoken in Brazil",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },

    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "What wrote Harry Potter",
        "options": ["A. JK Rowling", "B. Mark Twain", "C. no clue", "D. Harper Lee"],
        "answer": "A"
    }

]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct\n")
            score +=1
        else:
            print("Wrong, the correct answer is ", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)


