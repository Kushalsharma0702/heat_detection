import cv2
import numpy as np
import pyttsx3

# Initialize the pyttsx3 engine for the alarm sound
engine = pyttsx3.init()

# Function to trigger alarm sound
def trigger_alarm():
    engine.say("Fire detected! Alert!")
    engine.runAndWait()
    print("Fire detected! Alarm triggered.")

# Function to detect fire based on color detection
def detect_fire(frame):
    # Convert the frame to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of colors that are typically associated with fire (flame colors)
    lower_red = np.array([0, 150, 150])  # Lower bound for red color in HSV
    upper_red = np.array([10, 255, 255])  # Upper bound for red color in HSV

    # Create a mask that identifies pixels within the fire color range
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # You can adjust this range depending on your setup
    lower_yellow = np.array([20, 150, 150])
    upper_yellow = np.array([30, 255, 255])
    
    # Another mask for detecting yellow flame color
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Combine both masks to capture red and yellow flames
    fire_mask = cv2.bitwise_or(mask, mask_yellow)

    # Apply the mask to the original frame to get the flame areas
    fire_detected = cv2.bitwise_and(frame, frame, mask=fire_mask)

    # If there is a significant amount of fire detected, trigger the alarm
    if np.sum(fire_mask) > 10000:  # You can adjust the threshold based on your setup
        trigger_alarm()

    return fire_detected

# Start video capture (using the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    # Detect fire in the frame
    fire_frame = detect_fire(frame)

    # Show the frame with detected fire (if any)
    cv2.imshow("Fire Detection", fire_frame)
    
    # Wait for the user to press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
