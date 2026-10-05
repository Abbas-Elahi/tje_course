import random
import time

car1 = 0
car2 = 0
while car1 < 40 and car2 < 40:
    car1 += random.randint(1, 3)
    car2 += random.randint(1, 3)
    print("🚗 " + "-" * car1)
    print("🏎️ " + "-" * car2)
    print()
    time.sleep(0.2)
print("🚗 Car 1 wins!" if car1 > car2 else "🏎️ Car 2 wins!")
