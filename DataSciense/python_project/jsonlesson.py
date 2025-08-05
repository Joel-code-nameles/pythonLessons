import json
import time

commands = {
     "Hi there": "Hello! 😊 How can I assist you today?",
     "What can you do": "I can help anwer your questions, assist with tasks, provide recommendations, and more. What do you need help with?",
     "Whats the weather like today": "Sure! Can you tell me your location so I can check the local weather for you?",
     "Who made you": "I was created by developers using AI technology, trained to help lonely people like you!",
     "Tell me a joke": "Why don’t skeletons fight each other? Because they don’t have the guts! 😄",
     "Can you play music": "I can't play music directly, but I can recommend songs or generate playlists if you'd like!",
     "How old are you": "I don’t age like humans. I’m always learning and improving!",
     "What’s your name": "I am Liger your friendly Chatbot",
     "Can you help me with my homework": "Absolutely! Tell me the subject and question, and I’ll do my best to help.",
     "I am bored. What should I do": "How about a fun quiz, a brain teaser, or learning a random fact? I’ve got plenty of ideas!",
     "What time is it": f"Let me check... It's {time.strftime("%I :%M %p")}.",
     "How do I reset my password": "To reset your password, click on 'Forgot Password' on the login screen and follow the steps.",
     "Where is the nearest restaurant": "I can help with that! Please share your location so I can search nearby options.",
     "Translate 'Hello' into Spanish": "“Hello” in Spanish is “Hola.”",
     "Whats the capital of France": "The capital of France is Paris.",
     "Can I speak to a human": "Sure! Let me connect you with a human assistant. Just a moment.",
     "Are you real": "I’m not a person, but I’m very real in the digital world. Think of me as your smart assistant.",
     "What is 345 × 67": "Let me do the math… That’s 23,115.",
     "Can you set a reminder": "I can help suggest reminders, but you’ll need to set it in your device’s calendar or app.",
     "Goodbye": "Goodbye! Have a wonderful day. Come back anytime. 😊"
 }

with open('commands.json', "w") as command:
    json.dump(commands,command,indent=4,sort_keys=True)