import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tajassom Elm - Gravity Lab")

clock = pygame.time.Clock()

ball_x = 400
ball_y = 100
radius = 25

velocity_y = 0
gravity = 900

bounce = 0.75

ground_y = 540

running = True
resting = False

while running:

    dt = clock.tick(60) / 1000

    # --------------------
    # EVENTS
    # --------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                ball_y = 100
                velocity_y = 0
                resting = False

    # --------------------
    # PHYSICS
    # --------------------

    if not resting:

        velocity_y += gravity * dt
        ball_y += velocity_y * dt

    # --------------------
    # COLLISION
    # --------------------

    if ball_y + radius >= ground_y:

        ball_y = ground_y - radius

        velocity_y = -velocity_y * bounce

        if abs(velocity_y) < 40:
            velocity_y = 0
            resting = True

    # --------------------
    # DRAW
    # --------------------

    screen.fill("black")

    pygame.draw.line(screen, "white", (0, ground_y), (WIDTH, ground_y), 3)

    pygame.draw.circle(screen, "orange", (ball_x, int(ball_y)), radius)

    pygame.display.flip()

pygame.quit()
