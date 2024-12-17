import led
import ultrasonicSensor

functionMap = {
    0: led.ledOn,
    1: led.ledOff,
    2: ultrasonicSensor.initDistanceSensor,
    3: ultrasonicSensor.getDistance
}

def callFunc(func: int,ID: int, pin0: int, pin1: int):
    print("Calling Function")
    functionMap[func](ID, pin0, pin1)