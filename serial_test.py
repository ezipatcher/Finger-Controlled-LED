import serial
import time

arduino = serial.Serial("COM5", 9600)
time.sleep(2)

print("Sending ON...")
arduino.write(b"1")
time.sleep(3)

print("Sending OFF...")
arduino.write(b"0")

arduino.close()

print("Test complete.")