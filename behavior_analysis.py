#import section. Imports the distance function from the scipy.spatial module, renaming it to dist for simplicity. We use the distance function to calculate the Euclidean Distances, which measure key points around  the eye.
from scipy.spatial import distance as dist

# Constants and Variables
EAR_THRESHOLD=0.3 #sets as threshold for the Eye Aspect Ratio(EAR). When the EAR falls below this values, it's considered that the eye is closed
CONSEC_FRAMES=3 #minimum number of consecutive frames with an EYE below the threshold to consider a completer blink
blink_counter=0 #tracks consecutive frames where the eye appears closed
blink_total=0 #keeps a running total of the detected blinks

#eye_aspect_ratio() function declaration and definition. This function calculates the Eye Aspect Ratio(EAR) using six landmark points around the eye
def eye_aspect_ratio(eye): #eye parameter, a list of 6 points representing the eye landmarks, which form the shape of an eye. The points are ordered such that you can calculate distances between top-bottom and left-right pairs.
    A=dist.euclidean(eye[1], eye[5]) #The euclidean distance between the top and bottom landmarks of the eye (points 1 and 5)
    B=dist.euclidean(eye[2],eye[4]) #Vertical distance between the inner top and bottom points of the eye(points 2 and 4)
    C=dist.euclidean(eye[0],eye[3]) #Horizontal distance between the two outer points of the eye( points 0 and 3)
    return(A+B)/(2.0*C) #EAR Formula

#Analyzing Eye Blinks
#analyze_behavior() function declaration and definition. This function checks each frame for signs of blinking based EAR value.
def analyze_behavior(frame): #frame parameter, represents the current image from which the eye landmarks are extracted (using the facial landmark detector)
    global blink_counter, blink_total
    ear=eye_aspect_ratio(...)#Calculate eye aspect ratio. This part needs actual coordinates in practice
    if ear<EAR_THRESHOLD: #check EAR against threshold
        blink_counter +=1 #if ear<EAR_THRESHOLD, increment blink_counter by 1, indicating eye is closed
    else: # else if ear>EAR_THRESHOLD eye is open
        if blink_counter>=CONSEC_FRAMES: #checks if eye was closed for at least CONSEC_FRAMES frames, which counts as a blink.
            blink_total += 1 #if a blink is detected. blink_total is incremented by 1
        blink_counter=0 #blink_counter is reset to 0 to start counting the next blink
    return blink_total>some_threshold #Replace w/your threshold. Compares blink_total against a defined threshold(EG. a number of blinks within a set time interval). This threshold is used to indicate if blinking is excessive, which might suggest drowsiness or intoxication.