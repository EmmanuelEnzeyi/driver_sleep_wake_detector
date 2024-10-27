# Import the required functions from other modules in the project directory
from camera import initialize_camera, capture_frame
from face_detection import detect_face_and_eyes
from behavior_analysis import analyze_behavior
from vehicle_control import lock_engine

# Main function declaration and definition
def monitor_driver():
    # Initializes the camera and returns a capture object
    cap = initialize_camera()
    while True:
        # Capture a single frame for processing
        frame = capture_frame(cap)
        
        # Detect face and eyes using MediaPipe (now adapted to work with MediaPipe landmarks)
        face_landmarks = detect_face_and_eyes(frame)
        
        # Check if landmarks are detected
        if face_landmarks:
            # Analyzes behavior for signs of intoxication or drowsiness
            if analyze_behavior(face_landmarks, frame):
                lock_engine()  # Locks the engine if intoxicated behavior is detected
                print("Driver intoxicated. Engine Locked!")  # Message indicating the engine is locked
                break  # Exits the monitoring loop

    # Release the camera resource once the loop is exited
    cap.release()

# Run the program
if __name__ == "__main__":
    monitor_driver()
