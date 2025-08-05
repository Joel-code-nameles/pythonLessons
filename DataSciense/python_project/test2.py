import random
import time

print("🎯 WELCOME TO TERMINAL SHOOTER 2025 🎯")
print("Enemies are incoming! Type 'shoot' to blast 'em before they get you!")
print("Type 'quit' to exit the game.")
print("-----------------------------------------\n")

score = 0
lives = 3
enemy_delay = 3  # seconds between enemy spawns

while lives > 0:
    enemy_coming = random.choice([True, False])

    if enemy_coming:
        print("🚨 ENEMY APPROACHING! 🚨")
        start = time.time()
        action = input(">>> TYPE 'shoot' FAST: ").lower()
        end = time.time()

        if action == 'shoot' and (end - start) <= 2:
            print("💥 NICE SHOT! Enemy down.\n")
            score += 1
        elif action == 'quit':
            break
        else:
            print("😵 TOO SLOW! You got hit.\n")
            lives -= 1
    else:
        print("... No enemies right now. Stay ready.")
        time.sleep(1.5)

print("\n💀 GAME OVER 💀")
print(f"Your Score: {score}")
print("Come back stronger, legend. 🫡")
