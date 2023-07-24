/home/jknox/code/jknoxdev/video-lan-checker/incubator/mpolux.py
  1: import machine
  2: #import os
  3: import time
  4: import threading
  5: 
  6: 
  7: 
  8: # Pin definitions
  9: button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)  # Button pin, change the pin number accordingly
 10: led_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(1, 13)]  # RGB LED pins, adjust as per your setup
 11: 
 12: # Define modes and pin configurations
 13: modes = [
 14:     {'name': '8-bit', 'pins': [1, 2, 3, 4, 8, 9, 10, 11]},
 15:     {'name': '12-channel', 'pins': list(range(1, 13))},
 16:     {'name': '16-channel', 'pins': list(range(1, 13))},
 17:     {'name': '24-channel', 'pins': list(range(1, 13))},
 18: ]
 19: 
 20: current_mode = 0
 21: 
 22: def button_callback(pin):
 23:     global current_mode
 24:     current_mode = (current_mode + 1) % len(modes)
 25:     print("Switching to mode:", modes[current_mode]['name'])
 26: 
 27: # Set up the interrupt for the button
 28: button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
 29: 
 30: def set_led_pwm(pwm_value):
 31:     for pin in led_pins:
 32:         pin.duty(pwm_value)
 33: 
 34: # Set up PWM for RGB LEDs
 35: pwm_frequency = 500  # Adjust the frequency as needed
 36: pwm_max_value = 1023  # Adjust this value based on your LED requirements
 37: pwm_leds = [machine.PWM(pin, freq=pwm_frequency, duty=0) for pin in led_pins]
 38: 
 39: # Main loop
 40: while True:
 41:     mode = modes[current_mode]
 42:     print("Current mode:", mode['name'])
 43: 
 44:     if mode['name'] == '24-channel':
 45:         # Toggle 12 pins at a time with a 50% duty cycle for each row
 46:         for i in range(0, 12):
 47:             set_led_pwm(pwm_max_value if i < 6 else 0)  # Turn on first 6 pins
 48:             time.sleep(0.5)  # Adjust the delay as needed
 49:             set_led_pwm(pwm_max_value if i >= 6 else 0)  # Turn on last 6 pins
 50:             time.sleep(0.5)  # Adjust the delay as needed
 51:     else:
 52:         # Toggle all active pins with a 50% duty cycle
 53:         active_pins = mode['pins']
 54:         set_led_pwm(pwm_max_value)
 55:         time.sleep(0.5)  # Adjust the delay as needed
 56:         set_led_pwm(0)
 57:         time.sleep(0.5)  # Adjust the delay as needed
 58: 
 59: 
 60: # Set up the timer for LED refresh rate
 61: refresh_interval = 1.0  # Refresh rate in seconds, adjust as needed
 62: led_refresh_timer = None
 63: 
 64: def reset_led_refresh_timer():
 65:     global led_refresh_timer
 66:     if led_refresh_timer:
 67:         led_refresh_timer.cancel()
 68:     led_refresh_timer = threading.Timer(refresh_interval, refresh_leds)
 69:     led_refresh_timer.start()
 70: 
 71: def refresh_leds():
 72:     mode = modes[current_mode]
 73:     print("Current mode:", mode['name'])
 74: 
 75:     if mode['name'] == '24-channel':
 76:         # Toggle 12 pins at a time with a 50% duty cycle for each row
 77:         for i in range(0, 12):
 78:             set_led_pwm(pwm_max_value if i < 6 else 0)  # Turn on first 6 pins
 79:             time.sleep(0.5)  # Adjust the delay as needed
 80:             set_led_pwm(pwm_max_value if i >= 6 else 0)  # Turn on last 6 pins
 81:             time.sleep(0.5)  # Adjust the delay as needed
 82:     else:
 83:         # Toggle all active pins with a 50% duty cycle
 84:         active_pins = mode['pins']
 85:         set_led_pwm(pwm_max_value)
 86:         time.sleep(0.5)  # Adjust the delay as needed
 87:         set_led_pwm(0)
 88:         time.sleep(0.5)  # Adjust the delay as needed
 89: 
 90:     reset_led_refresh_timer()
 91: 
 92: def generate_led_status_string():
 93:     led_status_string = ""
 94:     for pwm_led in pwm_leds:
 95:         if pwm_led.duty() > 0:
 96:             led_status_string += "[*]"
 97:         else:
 98:             led_status_string += "[ ]"
 99:     return led_status_string
100: 
101: def print_status():
102:     mode = modes[current_mode]['name']
103:     led_status = generate_led_status_string()
104:     print(f"Current mode: {mode} | LED Status: {led_status}")
105: 
106: def refresh_leds():
107:     # Your previous LED control logic goes here
108: 
109:     # Call the print_status function to display the current status
110:     print_status()
111: 
112:     reset_led_refresh_timer()
113: 
114: # Main program loop
115: while True:
116:     # Your main program logic can go here if needed
117: 
118:     # Call the print_status function to display the current status
119:     print_status()
