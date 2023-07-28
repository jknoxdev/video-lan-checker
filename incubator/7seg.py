import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
DARK_GREY = (40, 40, 40)
WHITE = (255, 255, 255)

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
fullscreen = False  # New variable to store fullscreen mode state
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("LED 7-Segment Clock")

# Load font
font = pygame.font.Font(None, 200)

# Fading text variables
fade_duration = 3000  # Duration of the fading text in milliseconds
fade_start_time = None
fade_alpha = 255
fade_text = None

# Function to draw the clock display
# ... (unchanged code)

# Function to fade the text
# ... (unchanged code)

# Main game loop
running = True
paused = False
background_color = DARK_GREY
font_color = WHITE
updating_text = font.render("+inv: ", True, WHITE)
resize_text = None

# Initialize
window_resized = False
speed_update_text = font.render("", True, WHITE)
frame_start_time = 60
milliseconds_update = True

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            screen_width = event.w
            screen_height = event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            clock_width = int(screen_width * 0.8)
            clock_height = int(screen_height * 0.8)
            clock_x = (screen_width - clock_width) // 2
            clock_y = (screen_height - clock_height) // 2
            window_resized = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

            elif event.key == pygame.K_b:
                background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                font_color = (255 - background_color[0], 255 - background_color[1], 255 - background_color[2])
                fade_text_effect(updating_text)

            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS or event.key == pygame.K_p:
                # Increase refresh rate by 25ms (40fps)
                fps += 125
                speed_update_text = font.render("+125ms:" + str(fps), True, WHITE)
                fade_text_effect(speed_update_text)

            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS or event.key == pygame.K_m:
                # Decrease refresh rate by 25ms (or increase by 1000ms to prevent negative value)
                fps = int(max(1000 / 60, fps - 125))
                speed_update_text = font.render("-125ms: " + str(fps), True, WHITE)
                fade_text_effect(speed_update_text)
            elif event.key == pygame.K_s:  # Press 'S' to switch between 1 second and milliseconds update intervals
                milliseconds_update = not milliseconds_update
                if milliseconds_update:
                    update_rate_seconds = 0.001  # 1 millisecond update interval
                else:
                    update_rate_seconds = 1  # 1-second update interval
                fps = 1 / update_rate_seconds
            elif event.key == pygame.K_f:  # Press 'F' to toggle fullscreen mode
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                window_resized = True  # Trigger resizing event to handle clock display centering

    # Handle resizing event
    # ... (unchanged code)

    # Get the current time
    current_time = time.strftime("%H:%M:%S:") + str(int(time.time() * 1000) % 1000).zfill(3)

    # Only update and draw the clock display if not paused
    if not paused:
        # Draw the clock display
        draw_clock_display()

        # Print the current time in the console
        print(current_time)

    # Handle fading text effect
    # ... (unchanged code)

    clock.tick(fps)  # This will regulate the frame rate

    frame_start_time = pygame.time.get_ticks()

# Quit the program
pygame.quit()
