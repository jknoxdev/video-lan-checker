import pygame
import time

# Initialize pygame
pygame.init()

# Define colors
DARK_GREY = (40, 40, 40)
RED = (255, 0, 0)

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set the size of the clock display
clock_width = int(screen_width * 0.8)
clock_height = int(screen_height * 0.8)

# Calculate the position of the clock display
clock_x = (screen_width - clock_width) // 2
clock_y = (screen_height - clock_height) // 2

# Set the frame rate (60fps)
fps = 60
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("LED 7-Segment Clock")

# Load font
font = pygame.font.Font("./fonts/7SEGMENTALDIGITALDISPLAY.ttf", 200)

# Function to draw the clock display
def draw_clock_display():
    # Clear the screen with dark grey color
    screen.fill(DARK_GREY)

    # Render the current time as text
    # Include milliseconds
    current_time = time.strftime("%H:%M:%S:") + str(int(time.time() * 1000) % 1000).zfill(3)    
    text = font.render(current_time, True, RED)

    # Get the dimensions of the rendered text
    text_rect = text.get_rect()

    # Center the text in the clock display
    text_rect.center = (clock_x + clock_width // 2, clock_y + clock_height // 2)

    # Draw the text
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time
    current_time = time.strftime("%H:%M:%S:") + str(int(time.time() * 1000) % 1000).zfill(3)

    # Draw the clock display
    draw_clock_display()

    # Print the current time in the console
    print(current_time)

    # Limit the frame rate
    clock.tick(fps)

# Quit the program
pygame.quit()
