The YOLO-CarCounter-with-cv2 project is a vehicle detection and counting system that utilizes the power of YOLO (You Only Look Once) for object detection, and OpenCV for video processing and drawing detected objects and informational overlays on the video feed.

The system has the ability to detect vehicles like cars, trucks, buses, and motorbikes with high accuracy in real-time. After detection, it assigns unique IDs to each vehicle and tracks their movement across frames. Furthermore, it implements a virtual line in the video, and counts the vehicles crossing this line, providing a simple yet effective vehicle counting system.

An example of how the program works:

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/2122eeb3-390d-44d1-8ef6-0b6992a56c05)

Instructions:

Step 1: Import Necessary Libraries
Import all necessary libraries needed for the project. YOLO is used for object detection, cv2, and cvzone are used for image processing, and Sort is a simple online real-time tracking (SORT) algorithm.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/286f21e0-a7cd-4d94-9ef5-92f3f6052521)

Step 2: Initialize Variables and Load Model
Here we initialize the video capture, load the YOLO model for object detection, and define the line across which the cars will be counted. We also create an empty list to store the IDs of the counted vehicles.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/125559ea-26f8-477e-8569-13457d0e7611)

Step 3: Initialize Tracker
Initialize the SORT object tracker.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/e8c83d22-d68d-493e-a546-dceae6a8f2fc)

Step 4: Frame Capture and Processing
Capture the current frame, feed it to the YOLO model for object detection, and initialize the detection list.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/d401237c-a46b-45a0-aa6e-c9491f0ba398)

Step 5: Process Detected Objects
For each object detected by the YOLO model, process the bounding boxes, calculate confidence scores, and filter objects based on class and confidence score. Valid objects are added to the detections list.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/d7280aa8-5523-4dcf-a371-d2ed375b4829)

Step 6:  Object Tracking
Feed the detections to the SORT tracker to get the tracking results and draw the line where the count takes place.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/a1d0e848-83ef-4bdf-a782-a38d8bb9c68e)

Step 7: Display Result and Loop
Display the count on the frame, show the frame in a window, and wait for a key event. Loop back to Step 4.

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/a0ce63f0-2f4c-4b3e-8b3a-66d5d9d5eba3)



