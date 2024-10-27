#import section
import cv2 #imports the OpenCV library, which is abbreaviated as cv2 in python

#initialize_camera() function declaration and definition. Function intializes camera and prepares it for capturing video
def initialize_camera():
    return cv2.VideoCapture(0) #creates a video capture object using the default camera, indexed as 0, usually the built-in or primary web cam on a device
    #object returned by function is stored in a variable, and the variable is used to access the camera for capturing frames
    #if you have multiple cameras you can replace 0, with 1,2, ETC to select a different camera

#capture_frame() function declaration and definition. Function captures a single frame from the video feed and returns it for further processing
def capture_frame(cap): #cap is the video capture object returned by the initialize_camera() function
    ret, frame=cap.read() #reads a frame from the camera. ret is a boolean indicating wether the frame was successfully captured. if True, the frame capture was successfull
    if not ret: #if the frame capture was not captured, we're given a step which is to print out a message
        print("ERROR: Could not capture frame.")
        
    return frame #if the capture was successfull, the capture frame is returned for processing