from gpiozero import LED

def ledOn(pin):
    LED(pin).on()
    
def ledOff(pin):
    LED(pin).off()