import pyttsx3

QABot = pyttsx3.init()
qa_dataset = {
    "What is the boiling point of water": "100 degrees Celsius at sea level.",
    "What does CPU stand for": "Central Processing Unit.",
    "Who developed the theory of relativity": "Albert Einstein.",
    "What is the chemical symbol for gold": "Au.",
    "What is the capital of Ghana": "Accra.",
    "What is 7 x 8": "56.",
    "What planet is known as the Red Planet": "Mars.",
    "Define photosynthesis": "The process by which green plants make their food using sunlight.",
    "What is a URL": "Uniform Resource Locator.",
    "What is Newton's First Law of Motion": "An object will remain at rest or move in a straight line unless acted on by a force.",
}
person = input("Ask: ")

if person in qa_dataset:
    answer = qa_dataset[person]
    QABot.say(answer)
    QABot.runAndWait()