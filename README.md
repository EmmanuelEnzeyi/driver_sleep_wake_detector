# Driver Intoxication Detection System

## Project Overview
This project is a **Driver Intoxication Detection System** that utilizes facial recognition to detect signs of driver drowsiness or intoxication in real-time. Using **MediaPipe** and **OpenCV**, the system monitors the driver’s eye aspect ratio (EAR) and head movements. If intoxicated behavior is detected (e.g., excessive blinking, head tilting), the system will prevent the car from starting by locking the engine, ensuring safe driving practices.

## Table of Contents
- [Project Features](#project-features)
- [Technologies Used](#technologies-used)
- [Installation Requirements](#installation-requirements)
- [File Structure](#file-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Troubleshooting](#troubleshooting)

## Project Features
- **Real-Time Face Detection**: Uses MediaPipe Face Mesh for facial landmark detection.
- **Behavioral Analysis**: Tracks eye aspect ratio (EAR) and head tilt to identify drowsiness or intoxication.
- **Engine Lock Simulation**: If intoxicated behavior is detected, the system triggers an engine lock to prevent driving.
- **Cross-Platform Compatibility**: Can run on Windows, MacOS, and Linux, with support for multiple camera inputs.

## Technologies Used
- **Python** (3.6+)
- **OpenCV**: For video capture and processing.
- **MediaPipe**: For advanced facial landmark detection.

## Installation Requirements
To run this project, you need to have Python installed (version 3.6 or higher). Below are the libraries that need to be installed for the project to work:

### 1. OpenCV
Install OpenCV for video capture and image processing:
```bash
pip install opencv-python
```

### 2. MediaPipe
Install MediaPipe for facial landmark detection:
```bash
pip install mediapipe
```

### 3. SciPy
SciPy is used to calculate the Euclidean distances for eye aspect ratio (EAR) calculations:
```bash
pip install scipy
```

### Full Installation
To install all required packages at once, use:
```bash
pip install opencv-python mediapipe scipy
```

## File Structure
The project files are organized as follows:

```bash
Root Folder/
│
├── main.py                # Main script to run the driver monitoring system
├── camera.py              # Module for initializing and capturing frames from the camera
├── face_detection.py      # Module for detecting face and eye landmarks using MediaPipe
├── behavior_analysis.py   # Module for analyzing eye aspect ratio (EAR) and detecting signs of drowsiness/intoxication
├── vehicle_control.py     # Module simulating engine lock if intoxicated behavior is detected
└── README.md              # Project documentation
```

## How to Run the Project

### Clone the Repository
Clone this repository to your local machine.
```bash
git clone https://github.com/your-username/Driver_Intoxication_Detection.git
cd Driver_Intoxication_Detection
```

### Install Dependencies
Install the required libraries using the command below:
```bash
pip install opencv-python mediapipe scipy
```

### Run the Program
Execute the `main.py` file to start the driver monitoring system:
```bash
python main.py
```
The program will initialize the camera, detect the driver’s face, and begin monitoring for signs of drowsiness or intoxication. If intoxicated behavior is detected, a simulated engine lock will prevent further driving.

## Troubleshooting

### 1. OpenCV Import Issues
If OpenCV is not recognized, try reinstalling it using:
```bash
pip install --upgrade opencv-python
```

### 2. MediaPipe Compatibility
MediaPipe may have compatibility issues with some Python versions. Ensure you are using Python 3.6 or higher and try upgrading if needed.

### 3. Camera Access
Ensure your device has a functioning camera or external webcam connected. If using a different camera, change the index in `cv2.VideoCapture(0)` in `camera.py`.

### 4. Running on Virtual Environments
If using a virtual environment, make sure you have installed the dependencies within that environment.

---
