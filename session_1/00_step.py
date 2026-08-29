# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# ------------------------------------------------------
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# running = True


# while running:
#     screen.fill("black")


# pygame.quit()
# ------------------------------------------------------
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# running = True


# while running:
#     screen.fill("black")
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()
# ------------------------------------------------------
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# running = True


# while running:
#     screen.fill("black")
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, "yellow", (400, 100), 25)
# pygame.quit()

# ----------------------------------------------------------
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# running = True


# while running:
#     screen.fill("black")
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, "yellow", (400, 100), 25)
#     pygame.display.flip()
# pygame.quit()

# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     ball_y += 1

#     screen.fill("black")

#     pygame.draw.circle(screen, "orange", (ball_x, ball_y), 25)

#     pygame.display.flip()

# pygame.quit()
# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# velocity_y = 2

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     ball_y += velocity_y

#     screen.fill("black")

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), 25)

#     pygame.display.flip()

# pygame.quit()
# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# velocity_y = 0
# gravity = 0.1

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     velocity_y += gravity
#     ball_y += velocity_y

#     screen.fill("black")

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), 25)

#     pygame.display.flip()

# pygame.quit()
# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# radius = 25

# velocity_y = 0
# gravity = 0.1

# ground_y = 500

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     velocity_y += gravity
#     ball_y += velocity_y

#     if ball_y + radius >= ground_y:
#         ball_y = ground_y - radius

#     screen.fill("black")

#     pygame.draw.line(screen, "white", (0, ground_y), (800, ground_y), 3)

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

#     pygame.display.flip()

# pygame.quit()
# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# radius = 25

# velocity_y = 0
# gravity = 0.1

# ground_y = 500

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     velocity_y += gravity
#     ball_y += velocity_y

#     if ball_y + radius >= ground_y:

#         ball_y = ground_y - radius
#         velocity_y = -velocity_y

#     screen.fill("black")

#     pygame.draw.line(screen, "white", (0, ground_y), (800, ground_y), 3)

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

#     pygame.display.flip()

# pygame.quit()
# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# radius = 25

# velocity_y = 0
# gravity = 0.1

# bounce = 0.75

# ground_y = 500

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     velocity_y += gravity
#     ball_y += velocity_y

#     if ball_y + radius >= ground_y:

#         ball_y = ground_y - radius
#         velocity_y = -velocity_y * bounce

#     screen.fill("black")

#     pygame.draw.line(screen, "white", (0, ground_y), (800, ground_y), 3)

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

#     pygame.display.flip()

# pygame.quit()
# ----------------------------------------------------------
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# ball_x = 400
# ball_y = 100

# radius = 25

# velocity_y = 0
# gravity = 0.1

# bounce = 0.75

# ground_y = 500

# running = True
# resting = False

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     if not resting:
#         velocity_y += gravity
#         ball_y += velocity_y

#     if ball_y + radius >= ground_y:

#         ball_y = ground_y - radius
#         velocity_y = -velocity_y * bounce

#         if abs(velocity_y) < 1:
#             velocity_y = 0
#             resting = True

#     screen.fill("black")

#     pygame.draw.line(screen, "white", (0, ground_y), (800, ground_y), 3)

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

#     pygame.display.flip()

# pygame.quit()
# ---------------------------------------------------
# import pygame

# pygame.init()

# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# clock = pygame.time.Clock()

# ball_x = 400
# ball_y = 100

# radius = 25

# velocity_y = 0
# gravity = 900

# bounce = 0.75

# ground_y = 540

# running = True
# resting = False

# while running:

#     dt = clock.tick(60) / 1000

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#     if not resting:

#         velocity_y += gravity * dt
#         ball_y += velocity_y * dt

#     if ball_y + radius >= ground_y:

#         ball_y = ground_y - radius

#         velocity_y = -velocity_y * bounce

#         if abs(velocity_y) < 40:

#             velocity_y = 0
#             resting = True

#     screen.fill("black")

#     pygame.draw.line(screen, "white", (0, ground_y), (WIDTH, ground_y), 3)

#     pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

#     pygame.display.flip()

# pygame.quit()
# ---------------------------------------------------------
import pygame

# --------------------
# INITIALIZATION
# --------------------

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tajassom Elm - Gravity Lab")

clock = pygame.time.Clock()

# --------------------
# BALL SETTINGS
# --------------------

ball_x = 400
ball_y = 100

radius = 25

velocity_y = 0
gravity = 900

bounce = 0.75

# --------------------
# GROUND
# --------------------

ground_y = 540

# --------------------
# PROGRAM STATE
# --------------------

running = True
resting = False

# --------------------
# MAIN LOOP
# --------------------

while running:

    # Time passed since previous frame (seconds)
    dt = clock.tick(60) / 1000

    # --------------------
    # EVENTS
    # --------------------

    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:

            # Press R to reset the ball
            if event.key == pygame.K_r:
                ball_y = 100
                velocity_y = 0
                resting = False

    # --------------------
    # PHYSICS
    # --------------------

    if not resting:

        # Gravity changes velocity
        velocity_y += gravity * dt

        # Velocity changes position
        ball_y += velocity_y * dt

    # --------------------
    # COLLISION
    # --------------------

    if ball_y + radius >= ground_y:

        # Put the ball exactly on the ground
        ball_y = ground_y - radius

        # Reverse velocity and lose some energy
        velocity_y = -velocity_y * bounce

        # Stop very small bounces
        if abs(velocity_y) < 40:
            velocity_y = 0
            resting = True

    # --------------------
    # DRAW
    # --------------------

    screen.fill("black")

    # Draw ground
    pygame.draw.line(screen, "white", (0, ground_y), (WIDTH, ground_y), 3)

    # Draw ball
    pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

    pygame.display.flip()

# --------------------
# EXIT
# --------------------

pygame.quit()
