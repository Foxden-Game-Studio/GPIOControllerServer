import led

functionMap = {
    '0': led.ledOn,
    '1': led.ledOff
}

def callFunc(func: int, pin: int):
    functionMap[func](pin)