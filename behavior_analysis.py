# Import the necessary module
from scipy.spatial import distance as dist

# Constants and Variables
EAR_THRESHOLD = 0.3  # Threshold for detecting a closed eye
CONSEC_FRAMES = 3  # Frames needed to count as a blink
BLINK_THRESHOLD = 30  # Total blinks in a minute that might indicate drowsiness or intoxication

blink_counter = 0  # Tracks consecutive frames with closed eyes
blink_total = 0  # Running total of detected blinks

# Calculates the Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])  # Vertical distance (top-bottom)
    B = dist.euclidean(eye[2], eye[4])  # Vertical distance (inner top-bottom)
    C = dist.euclidean(eye[0], eye[3])  # Horizontal distance (left-right)
    return (A + B) / (2.0 * C)  # EAR formula

# Analyze behavior based on EAR and blinks
def analyze_behavior(landmarks, frame):
    global blink_counter, blink_total
    
    # Calculate EAR using eye landmarks for left and right eyes
    left_eye = [(landmarks[i].x * frame.shape[1], landmarks[i].y * frame.shape[0]) for i in [33, 160, 158, 133, 153, 144]]
    right_eye = [(landmarks[i].x * frame.shape[1], landmarks[i].y * frame.shape[0]) for i in [362, 385, 387, 263, 373, 380]]
    
    # Calculate EAR for each eye
    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)
    
    # Average EAR for both eyes
    ear = (left_ear + right_ear) / 2.0

    # Blink detection based on EAR threshold
    if ear < EAR_THRESHOLD:
        blink_counter += 1
    else:
        if blink_counter >= CONSEC_FRAMES:
            blink_total += 1
        blink_counter = 0  # Reset for the next potential blink

    # Check if blink rate exceeds threshold
    return blink_total > BLINK_THRESHOLD
