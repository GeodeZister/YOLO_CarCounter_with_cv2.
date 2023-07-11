import numpy as np
import cv2
import cvzone
import math
import time
from ultralytics import YOLO
from sort import Sort

# Constants
LIMITS = [350, 350, 950, 350]
DETECTION_CLASSES = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                     "traffic light", "fire hydrant"]
DETECTION_CONFIDENCE_THRESHOLD = 0.4
VIDEO_PATH = "../CarProject/traffic.mp4"
YOLO_MODEL_PATH = "../CarProject/yolov8l.pt"

# Initialize
totalCount = []
model = YOLO(YOLO_MODEL_PATH)
tracker = Sort(max_age=30, min_hits=2, iou_threshold=0.3)
cap = cv2.VideoCapture(VIDEO_PATH)


def process_image(img):
    results = model(img, stream=True)
    detections = np.empty((0, 5))

    # Process each result
    for r in results:
        for box in r.boxes:
            process_box(box, img, detections)

    # Update tracker
    results_tracker = tracker.update(detections)
    update_frame(img, results_tracker)

    return img


def process_box(box, img, detections):
    # Bounding Box
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Class Name
    cls = int(box.cls[0])
    current_class = DETECTION_CLASSES[cls]

    # Confidence
    conf = math.ceil((box.conf[0] * 100)) / 100

    if current_class in ['car', 'truck', 'bus', 'motorbike'] and conf > DETECTION_CONFIDENCE_THRESHOLD:
        cvzone.putTextRect(img, f'{DETECTION_CLASSES[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1,
                           colorR=(0, 0, 0), offset=1)
        current_array = np.array([x1, y1, x2, y2, conf])
        detections = np.vstack((detections, current_array))


def update_frame(img, results_tracker):
    cv2.line(img, (LIMITS[0], LIMITS[1]), (LIMITS[2], LIMITS[3]), (0, 0, 255), 2)

    for result in results_tracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = map(int, result[:4])
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=1, colorR=(255, 165, 0), colorC=(0, 255, 255))
        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 1, (255, 255, 140))

        if LIMITS[0] < cx < LIMITS[2] and LIMITS[1] - 15 < cy < LIMITS[1] + 15:
            if id not in totalCount:
                cv2.line(img, (LIMITS[0], LIMITS[1]), (LIMITS[2], LIMITS[3]), (0, 255, 0), 2)
                totalCount.append(id)

    cvzone.putTextRect(img, f'Count: {len(totalCount)}', (50, 50), scale=3, thickness=4,
                       colorR=(0, 0, 0), offset=5)


def main():
    while True:
        new_frame_time = time.time()
        success, img = cap.read()

        if not success:
            break

        img = process_image(img)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
