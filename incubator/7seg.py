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

            # ... (previous key events)

            elif event.key == pygame.K_f:  # Press 'F' to toggle fullscreen mode
                fullscreen = not fullscreen
                if fullscreen:
                    # Get the native screen resolution
                    modes = pygame.display.list_modes()
                    native_width, native_height = modes[0]
                    # screen = pygame.display.set_mode((native_width, native_height), pygame.FULLSCREEN)
            
                    # Get the native screen
                    # info = pygame.display.Info()
                    # native_width, native_height = info.current_w, info.current_h
                    screen = pygame.display.set_mode((native_width, native_height), pygame.FULLSCREEN)
                    # Redraw the clock display
                    clock_width = int(native_width * 0.8)
                    clock_height = int(native_height * 0.8)
                    clock_x = (native_width - clock_width) // 2
                    clock_y = (native_height - clock_height) // 2
                    draw_clock_display()

                    # Output the screen resolution to the console
                    print(f"Screen resolution: {native_width}x{native_height}")
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                    # Redraw the clock display
                    clock_width = int(screen_width * 0.8)
                    clock_height = int(screen_height * 0.8)
                    clock_x = (screen_width - clock_width) // 2
                    clock_y = (screen_height - clock_height) // 2
                    draw_clock_display()

                    # Output the screen resolution to the console
                    print(f"Screen resolution: {screen_width}x{screen_height}")
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
