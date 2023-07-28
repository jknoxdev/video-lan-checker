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
def draw_clock_display():
    # Clear the screen with current background color
    screen.fill(background_color)

    # Render the current time as text
    # Include milliseconds
    current_time = time.strftime("%H:%M:%S:") + str(int(time.time() * 1000) % 1000).zfill(3)
    text = font.render(current_time, True, font_color)

    # Get the dimensions of the rendered text
    text_rect = text.get_rect()

    # Center the text in the clock display
    text_rect.center = (clock_x + clock_width // 2, clock_y + clock_height // 2)

    # Draw the text
    screen.blit(text, text_rect)

    # Draw the fading text if available
    if fade_text:
        fade_text.set_alpha(fade_alpha)
        fade_text_rect = fade_text.get_rect()
        fade_text_rect.center = (clock_x + clock_width // 2, clock_y + clock_height // 6)
        screen.blit(fade_text, fade_text_rect)

    # Invert the LED segments color
    inverted_background_color = (255 - background_color[0], 255 - background_color[1], 255 - background_color[2])
    inverted_font_color = (255 - font_color[0], 255 - font_color[1], 255 - font_color[2])

    # Update the display
    pygame.display.flip()

# Function to fade the text
def fade_text_effect(text):
    global fade_start_time, fade_alpha, fade_text

    fade_start_time = pygame.time.get_ticks()
    fade_alpha = 255
    fade_text = text

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

    # Additional event handling for fullscreen mode
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        paused = not paused
    if keys[pygame.K_b]:
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        font_color = (255 - background_color[0], 255 - background_color[1], 255 - background_color[2])
        fade_text_effect(updating_text)
    if keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS] or keys[pygame.K_p]:
        fps += 125
        speed_update_text = font.render("+125ms:" + str(fps), True, WHITE)
        fade_text_effect(speed_update_text)
    if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS] or keys[pygame.K_m]:
        fps = int(max(1000 / 60, fps - 125))
        speed_update_text = font.render("-125ms: " + str(fps), True, WHITE)
        fade_text_effect(speed_update_text)
    if keys[pygame.K_s]:  # Press 'S' to switch between 1 second and milliseconds update intervals
        milliseconds_update = not milliseconds_update
        if milliseconds_update:
            update_rate_seconds = 0.001  # 1 millisecond update interval
        else:
            update_rate_seconds = 1  # 1-second update interval
        fps = 1 / update_rate_seconds
    if keys[pygame.K_f]:  # Press 'F' to toggle fullscreen mode
        fullscreen = not fullscreen
        if fullscreen:
            modes = pygame.display.list_modes()
            native_width, native_height = modes[0]
            screen = pygame.display.set_mode((native_width, native_height), pygame.FULLSCREEN)
            clock_width = int(native_width * 0.8)
            clock_height = int(native_height * 0.8)
            clock_x = (native_width - clock_width) // 2
            clock_y = (native_height - clock_height) // 2
            draw_clock_display()
            print(f"Screen resolution: {native_width}x{native_height}")
        else:
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            clock_width = int(screen_width * 0.8)
            clock_height = int(screen_height * 0.8)
            clock_x = (screen_width - clock_width) // 2
            clock_y = (screen_height - clock_height) // 2
            draw_clock_display()
            print(f"Screen resolution: {screen_width}x{screen_height}")
        window_resized = True

    # Handle resizing event
    if window_resized:
        resize_text = font.render(f"Resized: {screen_width}x{screen_height}", True, WHITE)
        fade_text_effect(resize_text)
        window_resized = False

    # Get the current time
    current_time = time.strftime("%H:%M:%S:") + str(int(time.time() * 1000) % 1000).zfill(3)

    # Only update and draw the clock display if not paused
    if not paused:
        # Draw the clock display
        draw_clock_display()

        # Print the current time in the console
        print(current_time)

    # Handle fading text effect
    if fade_text and fade_alpha > 0:
        elapsed_time = pygame.time.get_ticks() - fade_start_time
        if elapsed_time > fade_duration:
            fade_text = None
        else:
            fade_alpha = 255 - int((elapsed_time / fade_duration) * 255)

    clock.tick(fps)  # This will regulate the frame rate
    frame_start_time = pygame.time.get_ticks()

# Quit the program
pygame.quit()
