import cv2  # OpenCV for capturing and displaying frames
import mediapipe as mp  # MediaPipe for facial landmark detection

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

def detect_face_and_eyes(frame):
    """
    Detects face and eye landmarks in the given frame.

    Parameters:
        frame: The image in which the function will look for faces and eyes. 
               Usually, it's a frame from a video feed or a single image.

    Returns:
        face_landmarks: The detected landmarks if a face is detected, None otherwise.
    """
    # Convert the frame to RGB as MediaPipe expects RGB images
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe Face Mesh
    results = face_mesh.process(rgb_frame)
    
    # Check if any face landmarks are detected
    if results.multi_face_landmarks:
        # Return landmarks of the first detected face
        return results.multi_face_landmarks[0].landmark
    else:
        return None  # Return None if no face is detected
