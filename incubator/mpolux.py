import machine
import time
import threading



# Pin definitions
button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)  # Button pin, change the pin number accordingly
led_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(1, 13)]  # RGB LED pins, adjust as per your setup

# Define modes and pin configurations
modes = [
    {'name': '8-bit', 'pins': [1, 2, 3, 4, 8, 9, 10, 11]},
    {'name': '12-channel', 'pins': list(range(1, 13))},
    {'name': '16-channel', 'pins': list(range(1, 13))},
    {'name': '24-channel', 'pins': list(range(1, 13))},
]

current_mode = 0

def button_callback(pin):
    global current_mode
    current_mode = (current_mode + 1) % len(modes)
    print("Switching to mode:", modes[current_mode]['name'])

# Set up the interrupt for the button
button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

def set_led_pwm(pwm_value):
    for pin in led_pins:
        pin.duty(pwm_value)

# Set up PWM for RGB LEDs
pwm_frequency = 500  # Adjust the frequency as needed
pwm_max_value = 1023  # Adjust this value based on your LED requirements
pwm_leds = [machine.PWM(pin, freq=pwm_frequency, duty=0) for pin in led_pins]

# Main loop
while True:
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

def generate_led_status_string():
    led_status_string = ""
    for pwm_led in pwm_leds:
        if pwm_led.duty() > 0:
            led_status_string += "[*]"
        else:
            led_status_string += "[ ]"
    return led_status_string

def print_status():
    mode = modes[current_mode]['name']
    led_status = generate_led_status_string()
    print(f"Current mode: {mode} | LED Status: {led_status}")

def refresh_leds():
    # Your previous LED control logic goes here

    # Call the print_status function to display the current status
    print_status()

    reset_led_refresh_timer()

# Main program loop
while True:
    # Your main program logic can go here if needed

    # Call the print_status function to display the current status
    print_status()
