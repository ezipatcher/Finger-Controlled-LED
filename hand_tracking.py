import cv2
import mediapipe as mp
import math
import serial
import time

# Arduino connection
arduino = serial.Serial("COM5", 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

THRESHOLD = 60
previous_state = None

while True:

    success, frame = cap.read()

    if not success:
        print("Could not access webcam.")
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    led_state = "LED OFF"

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]

            h, w, _ = frame.shape

            thumb_x = int(thumb.x * w)
            thumb_y = int(thumb.y * h)

            index_x = int(index.x * w)
            index_y = int(index.y * h)

            distance = math.sqrt(
                (index_x - thumb_x) ** 2 +
                (index_y - thumb_y) ** 2
            )

            cv2.line(
                frame,
                (thumb_x, thumb_y),
                (index_x, index_y),
                (255, 0, 0),
                3
            )

            if distance <= THRESHOLD:
                led_state = "LED ON"
                current_state = "1"
            else:
                led_state = "LED OFF"
                current_state = "0"

            # Send only when the state changes
            if current_state != previous_state:
                arduino.write(current_state.encode())
                previous_state = current_state

            cv2.putText(
                frame,
                f"Distance: {int(distance)}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.putText(
        frame,
        led_state,
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3
    )

    cv2.imshow("Finger Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()