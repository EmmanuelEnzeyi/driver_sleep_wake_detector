import cv2  # Imports the OpenCV library for handling video capture

# Initializes the camera and prepares it for capturing video
def initialize_camera():
    cap = cv2.VideoCapture(0)  # Create a VideoCapture object with the primary camera
    if not cap.isOpened():  # Check if the camera opened successfully
        print("ERROR: Could not open the camera.")
    return cap  # Return the capture object to access the camera for capturing frames

# Captures a single frame from the video feed and returns it for processing
def capture_frame(cap):  # cap is the VideoCapture object returned by initialize_camera()
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:  # If the frame capture failed
        print("ERROR: Could not capture frame.")
        return None  # Return None if frame capture fails
    return frame  # If successful, return the captured frame for processing
