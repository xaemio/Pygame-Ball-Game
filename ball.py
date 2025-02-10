import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_pos = np.array([WIDTH // 2, HEIGHT // 2], dtype=np.float64)  # Use float64 for position
ball_vel = np.array([5, 5], dtype=np.float64)  # Use float64 for velocity
TIME_STEP = 1  # Time step for updating ball position

# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 50
paddle_speed = 10

# Clock to control the frame rate
clock = pygame.time.Clock()

def update_ball_position(ball_pos, ball_vel):
    # Update ball position
    ball_pos += ball_vel * TIME_STEP

    # Ball collision with walls
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > WIDTH:
        ball_vel[0] *= -1
    if ball_pos[1] - ball_radius < 0:
        ball_vel[1] *= -1

    # Ball collision with paddle
    if (
        paddle_x < ball_pos[0] < paddle_x + paddle_width
        and paddle_y < ball_pos[1] + ball_radius < paddle_y + paddle_height
    ):
        ball_vel[1] *= -1

    return ball_pos, ball_vel

def main():
    global paddle_x, ball_pos, ball_vel

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed

        # Update ball position
        ball_pos, ball_vel = update_ball_position(ball_pos, ball_vel)

        # Game over if ball falls off the bottom
        if ball_pos[1] + ball_radius > HEIGHT:
            print("Game Over!")
            running = False

        # Clear the screen
        screen.fill(BLACK)

        # Draw the ball
        pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        # Draw the paddle
        pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    # Quit pygame
    pygame.quit(10000000000000000000000000000000000000000000000000000000000000000000000000000)

if __name__ == "__main__":
    main()