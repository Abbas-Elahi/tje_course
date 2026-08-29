# -------------- variable & DataType---------------
score = 10  # Integer
player_x = 100
player_y = 200
health = 100

running = True  # Boolean
game_over = False

gravity = 0.8  # Float
velocity = 2.5

player_name = "Ali"  # String
game_title = "Space Game"

enemies = ["enemy1", "enemy2", "enemy3"]  # List
scores = [10, 20, 30, 40]

score = 10
score = score + 10
score += 10
# --------------- Conditions ----------------
if age > 18:
    print("your age is ok!")
else:
    print("your age is nokay!")


if score == 10:
    print("You win!")


health = 0
if health > 0:
    print("Player is alive")
else:
    print("Game Over")


score = 70
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Try again")


fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple exists")

# -------------------Loop ----------------
for i in range(5):
    print("Hello")


for i in range(5):
    print(i)


for i in range(1, 6):
    print(i)


names = ["Ali", "Sara", "Reza"]
for name in names:
    print(name)


number = 0
while number < 5:
    print(number)
    number += 1


running = True
while running:
    print("Game is running")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


state = "menu"
if state == "menu":
    print("Show menu")
elif state == "playing":
    print("Run game")
elif state == "game_over":
    print("Game Over")


import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.fill((0, 0, 0))
            pygame.display.flip()
            pygame.quit()


score = 0
running = True
while running:
    score += 1
    if score == 10:
        running = False
        print(score)
