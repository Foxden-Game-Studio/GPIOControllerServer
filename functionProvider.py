import led

functionMap = {
    0: led.ledOn,
    1: led.ledOff
}

def callFunc(func: int, pin: int):
    print("Calling Function")
    functionMap[func](pin)