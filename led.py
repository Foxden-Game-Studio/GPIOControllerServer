from gpiozero import LED

# Store LED objects for each pin
led_objects = {}

def ledOn(pin):
    if pin not in led_objects:
        led_objects[pin] = LED(pin)  # Create LED object for the pin
    led_objects[pin].on()  # Turn on the LED

def ledOff(pin):
    if pin in led_objects:
        led_objects[pin].off()  # Turn off the LED