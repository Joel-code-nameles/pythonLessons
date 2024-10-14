import pyttsx3 

vioce = pyttsx3.init()

vioce.say ("Do you want to know why B-GYM is the best gym")
vioce.runAndWait()

option = input(": ")

if option == ("yes"):
    vioce.say ("Becauce we open early,and we have the best fitnes trainers .")
    vioce.runAndWait()
else:
    vioce.say ("Why dont you want to learn lazy rat!")
    vioce.runAndWait()
