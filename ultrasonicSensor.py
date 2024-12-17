from gpiozero import DistanceSensor
from time import sleep

distanceSensor = {}
checkDistance = False

def initDistanceSensor(ID, trigPin, echoPin):
        distanceSensor[ID] = DistanceSensor(echoPin, trigPin)
        print("Distance Sensor Initialized!")

def getDistance(ID: int, delay: int, send_callback):
    global checkDistance
    if not checkDistance:
        print("Starting distance measurement...")
        checkDistance = True
        while checkDistance:
            if ID in distanceSensor:
                distance = distanceSensor[ID].distance * 100
                send_callback(distance)  # Send the distance to the client
                sleep(delay)
            else:
                print("Sensor ID not found!")
                break
    else:
        print("Stopping distance measurement...")
        checkDistance = False