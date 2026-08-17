# Gesture-Controlled LED

A computer-vision-based Arduino project that allows you to control an LED using a simple **thumb-and-index-finger gesture**.

The laptop webcam detects the user's hand using **MediaPipe**, calculates the distance between the thumb and index finger, and sends an ON/OFF command to an **Arduino UNO** through serial communication.

## Project Demo

**Gesture:**

* Thumb + index finger close → **LED ON**
* Thumb + index finger apart → **LED OFF**

## How It Works

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Tracking
   ↓
Detect Thumb & Index Finger
   ↓
Calculate Distance
   ↓
Distance ≤ Threshold?
   ↓
 ┌───────────────┐
 │               │
 YES             NO
 │               │
 ↓               ↓
Send "1"        Send "0"
 │               │
 └───────┬───────┘
         ↓
     Arduino UNO
         ↓
       LED
```

## Features

* Real-time hand tracking
* Thumb and index finger detection
* Gesture-based LED control
* Serial communication between Python and Arduino
* No external sensors required
* Uses a normal laptop webcam
* Simple and low-cost hardware

## Hardware Required

| Component             | Quantity |
| --------------------- | -------: |
| Arduino UNO           |        1 |
| LED                   |        1 |
| 220 Ω resistor        |        1 |
| Breadboard            |        1 |
| Jumper wires          |      2–3 |
| USB cable             |        1 |
| Laptop/PC with webcam |        1 |

## Circuit

```text
Arduino D13
     │
     ▼
  220 Ω
     │
     ▼
 LED (+)
 LED (−)
     │
     ▼
 Arduino GND
```

The resistor must be connected in series with the LED.

## Software Requirements

* Python 3.12
* OpenCV
* MediaPipe 0.10.21
* PySerial
* Arduino IDE

## Running the Project

First connect the Arduino UNO to your computer through USB.

Then run:

```bash
py -3.12 python/hand_tracking.py
```

A webcam window will open.

Move your thumb and index finger:

```text
Fingers close
      ↓
LED ON

Fingers apart
      ↓
LED OFF
```

Press **Q** to exit the program.

## Testing Serial Communication

Before running the complete project, you can test the Arduino connection using:

```bash
py -3.12 python/serial_test.py
```

The test sends:

```text
1 → LED ON
0 → LED OFF
```

## Technologies Used

* **Python**
* **OpenCV**
* **MediaPipe**
* **PySerial**
* **Arduino UNO**
* **C/C++**
* **Computer Vision**

## Future Improvements

* Control multiple LEDs using different gestures
* Add brightness control using finger distance
* Control a relay or other electronic devices
* Add multiple-hand gesture recognition
* Create a graphical user interface
* Replace the wired serial connection with wireless communication using ESP32

## Author

**Rupam**

Electronics and Communication Engineering Student

---

If you found this project useful, consider giving the repository a ⭐.
