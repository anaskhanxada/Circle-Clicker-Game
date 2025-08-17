import pygame as py
import random
import sys

# Initialize Pygame
py.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 400
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Circle Clicker Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
random_color = lambda: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Game variables
score = 0
time_limit = 30  # Game duration in seconds
clock = py.time.Clock()
font = py.font.Font(None, 36)
start_time = py.time.get_ticks()  # Game start time

# Function to draw a circle at a random position
def draw_circle():
    x = random.randint(20, WIDTH - 20)
    y = random.randint(20, HEIGHT - 20)
    radius = random.randint(10, 30)
    return {"pos": (x, y), "radius": radius, "color": random_color()}

# Generate the first circle
circle = draw_circle()

# Main game loop
while True:
    screen.fill(BLACK)
    
    # Timer
    elapsed_time = (py.time.get_ticks() - start_time) / 1000  # In seconds
    remaining_time = max(0, time_limit - elapsed_time)
    
    # Check if time is up
    if remaining_time <= 0:
        game_over_text = font.render("Game Over! Score: " + str(score), True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 20))
        py.display.flip()
        py.time.wait(3000)  # Wait for 3 seconds before closing
        py.quit()
        sys.exit()
    
    # Event handling
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            sys.exit()
        if ev.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            # Check if the click is inside the circle
            dist = ((pos[0] - circle["pos"][0]) ** 2 + (pos[1] - circle["pos"][1]) ** 2) ** 0.5
            if dist <= circle["radius"]:
                score += 1
                circle = draw_circle()  # Generate a new circle
    
    # Draw the current circle
    py.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])
    
    # Display score and timer
    score_text = font.render(f"Score: {score}", True, WHITE)
    timer_text = font.render(f"Time: {int(remaining_time)}s", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))
    
    # Update display
    py.display.flip()
    clock.tick(60)  # Limit to 60 FPS

