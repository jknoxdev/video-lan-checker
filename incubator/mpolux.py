import machine
import time
import threading

# ... (previous code)

# Set up the timer for LED refresh rate
refresh_interval = 1.0  # Refresh rate in seconds, adjust as needed
led_refresh_timer = None

def reset_led_refresh_timer():
    global led_refresh_timer
    if led_refresh_timer:
        led_refresh_timer.cancel()
    led_refresh_timer = threading.Timer(refresh_interval, refresh_leds)
    led_refresh_timer.start()

def refresh_leds():
    mode = modes[current_mode]
    print("Current mode:", mode['name'])

    if mode['name'] == '24-channel':
        # Toggle 12 pins at a time with a 50% duty cycle for each row
        for i in range(0, 12):
            set_led_pwm(pwm_max_value if i < 6 else 0)  # Turn on first 6 pins
            time.sleep(0.5)  # Adjust the delay as needed
            set_led_pwm(pwm_max_value if i >= 6 else 0)  # Turn on last 6 pins
            time.sleep(0.5)  # Adjust the delay as needed
    else:
        # Toggle all active pins with a 50% duty cycle
        active_pins = mode['pins']
        set_led_pwm(pwm_max_value)
        time.sleep(0.5)  # Adjust the delay as needed
        set_led_pwm(0)
        time.sleep(0.5)  # Adjust the delay as needed

    reset_led_refresh_timer()

# Main program loop
while True:
    # Your main program logic can go here if needed
    pass

# When exiting the loop, cancel the timer
if led_refresh_timer:
    led_refresh_timer.cancel()
