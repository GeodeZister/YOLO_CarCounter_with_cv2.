The YOLO-CarCounter-with-cv2 project is a vehicle detection and counting system that utilizes the power of YOLO (You Only Look Once) for object detection, and OpenCV for video processing and drawing detected objects and informational overlays on the video feed.

The system has the ability to detect vehicles like cars, trucks, buses, and motorbikes with high accuracy in real-time. After detection, it assigns unique IDs to each vehicle and tracks their movement across frames. Furthermore, it implements a virtual line in the video, and counts the vehicles crossing this line, providing a simple yet effective vehicle counting system.

An example of how the program works:

![image](https://github.com/GeodeZister/YOLO_CarCounter_with_cv2./assets/97829206/2122eeb3-390d-44d1-8ef6-0b6992a56c05)

Instructions:

Step 1: Import Necessary Libraries

Import all necessary libraries needed for the project. YOLO is used for object detection, cv2, and cvzone are used for image processing, and Sort is a simple online real-time tracking (SORT) algorithm.

<pre>
import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
import time
from sort import*
</pre>

Step 2: Initialize Variables and Load Model

Here we initialize the video capture, load the YOLO model for object detection, and define the line across which the cars will be counted. We also create an empty list to store the IDs of the counted vehicles.

<pre>cap = cv2.VideoCapture("../CarProject/traffic.mp4")
limits = [350,350, 950, 350]
totalCount = []
model = YOLO("../CarProject/yolov8l.pt")
</pre>

Step 3: Initialize Tracker

Initialize the SORT object tracker.
<pre>tracker = Sort(max_age=30, min_hits=2, iou_threshold=0.3)
</pre>

Step 4: Frame Capture and Processing

Capture the current frame, feed it to the YOLO model for object detection, and initialize the detection list.
<pre>
new_frame_time = time.time()
success, img = cap.read()
results = model(img, stream=True)
detections = np.empty((0,5))

</pre>

Step 5: Process Detected Objects

For each object detected by the YOLO model, process the bounding boxes, calculate confidence scores, and filter objects based on class and confidence score. Valid objects are added to the detections list.

<pre>
  for r in results:
    boxes = r.boxes
    for box in boxes:
        # code for processing each box and adding valid objects to detections list
</pre>

Step 6:  Object Tracking

Feed the detections to the SORT tracker to get the tracking results and draw the line where the count takes place.

<pre>
resultsTracker = tracker.update(detections)
cv2.line(img,(limits[0],limits[1]),(limits[2], limits[3]),(0,0,255),2)
</pre>

Step 7: Display Result and Loop

Display the count on the frame, show the frame in a window, and wait for a key event. Loop back to Step 4.

<pre>cvzone.putTextRect(img, f'Count: {len(totalCount)}', (50, 50), scale=3, thickness=4, colorR=(0, 0, 0), offset=5)
cv2.imshow("Image", img)
cv2.waitKey(1)
</pre>


