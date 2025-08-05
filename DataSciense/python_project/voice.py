import pyttsx3

family = ["Beatrice","Jason","Junior","Alma","Korda","Joel"]
operator = pyttsx3.init()
operator.say("Who is this?")
operator.runAndWait()
choice = input("Name: ")

if choice in family:
    operator.say(f"Welcome back {choice}")
    operator.runAndWait()


else:
    operator.say(f"I will hunt you down {choice} for trying to rob my house you stupid and idiotic human")
    operator.runAndWait()