#imports section, imports functions from the other modules(files) within this directory
from camera import initialize_camera, capture_frame
from face_detection import detect_face_and_eyes
from behavior_analysis import analyze_behavior
from vehicle_control import lock_engine

#main function declaration and definition: monitor_driver()
def monitor_driver():
    cap = initialize_camera() #initializes the camera and returns a cap object. This is what starts the camera
    while True: #starts an infinite loop to keep on capturing frames, untill the unexpected condition is seen
        frame=capture_frame(cap) #captures a single frame, then the frame will be processed in the next steps
        if detect_face_and_eyes(frame): #checks if the driver's face and eyes are present in the captured frame
            if analyze_behavior(frame): #analyzes the frame for signs of intoxicated behavior, like abnoramal blinking, head tilting, or gaze direction, if detected, program moves to next step
                lock_engine() #function to lock the engine, hence prevent the driver from driving
                print("Driver intoxicated. Engine Locked!") #outputs a message to indicate that the engine is locked
                break #exits the loop, ending the monitoring process
            cap.release() #releases the camera resource once the loop is exited, stopping the video capture

#running the program            
if __name__ == "__main__": #checks if the script is being run directly(not imported as a module) If it is, it calls the monitor_driver() function to start the program
    monitor_driver()
    