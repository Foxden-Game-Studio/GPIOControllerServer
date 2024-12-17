from gpiozero import LED

# Store LED objects for each pin
led_objects = {}

def ledOn(ID: int, pin0: int, pin1: int):
    if pin0 not in led_objects:
        led_objects[pin0] = LED(pin0)  # Create LED object for the pin
    led_objects[pin0].on()  # Turn on the LED

def ledOff(ID: int, pin0: int, pin1: int):
    if pin0 in led_objects:
        led_objects[pin0].off()  # Turn off the LED