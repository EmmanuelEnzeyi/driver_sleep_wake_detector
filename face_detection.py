#This is the code for face and eye detection with OpenCV

#import area. Importing the OpenCV library, which provides functions for image and video processing
import cv2

#face and eye classifiers. Haar cascades are ML based object detection methods, used for detecting faces and eyes
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #loads the pre-trained Haar cascade classifiers. Contains data to detect faces.
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') #points to where OpenCV stores pre-trained Haar cascade XML files. haarcascade_eye.xml, contains data to detect eyes
#when the above 2 lines are executed, face_cascade and eye_cascade objects are created, each loaded with the respective data needed to detect faces and eyes in an image.

def detect_face_and_eyes(frame): #The parameter frame, is the image in which the function will look for faces and eyes. Usually a frame froma video feed or a single image.
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #cv2.cvtColor() converts the frame from color(BGR) to grayscale.This simplifies the image and speeds up processing, as color information is not needed for detection.
    faces=face_cascade.detectMultiScale(gray,1.1,4) #scans the image for objects of varying sizes based on the face_cascade. gray(the grayscale image where faces are to be detected), 1.1(specifies how much the image size is reduced at each image scale, higher values make detection faster but may miss smaller faces),4(The minimum number neighbors each rectangle should have to retain it. Higher values reduce false positive) Each rectangle is represented as (x,y,w,h), where (x,y) is the top-left coordinate, and (w,h) are the width and height of the rectangle
    return any(faces) #Returns True if a face is detected. any(faces) checks if there is atleast one face detected. If there is, it returns True, otherwise, it returns False