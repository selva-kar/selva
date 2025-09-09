# Simple General Knowledge Quiz App
questions = {
    
"What is the capital of France?": "Paris",
    "Who wrote the theory of relativity?": "Einstein",
    "What planet is known as the Red Planet?": "Mars",
    "Who is known as the Father of Computers?": "Charles Babbage",
    "What is the chemical symbol for water?": "H2O",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What is the largest ocean on Earth?": "Pacific",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "In which year did the Titanic sink?": "1912",
    "What is the smallest prime number?": "2",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the hardest natural substance on Earth?": "Diamond",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "Which planet has the most moons?": "Saturn",
    "What is the capital city of Australia?": "Canberra",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What gas do plants absorb from the atmosphere?": "Carbon dioxide",
    "Which element has the chemical symbol 'O'?": "Oxygen",
    "How many continents are there on Earth?": "7",
    "What is the largest mammal?": "Blue whale",
    "Who was the first man to walk on the moon?": "Neil Armstrong",
    "What is the tallest mountain in the world?": "Mount Everest",
    "Which language has the most native speakers?": "Mandarin",
    "In which country did the Olympic Games originate?": "Greece",
    "What currency is used in Japan?": "Yen",
    "What is the boiling point of water in Celsius?": "100",
    "Who wrote the novel '1984'?": "George Orwell",
    "Which organ in the human body is primarily responsible for filtering blood?": "Kidney",
    "What is the longest river in the world?": "Nile",
    "Which famous scientist developed the laws of motion?": "Isaac Newton",
    "What is the name of the largest desert in the world?": "Sahara",
}

score = 0

for question, answer in questions.items():
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong. The correct answer is: {answer}")
    print()

print(f"🎯 Your total score is {score}/{len(questions)}")
