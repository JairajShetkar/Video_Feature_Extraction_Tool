from ultralytics import YOLO
import cv2

def person_object_ratio(video_path, sample_rate=30):
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    total_people = 0
    total_objects = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % sample_rate == 0:
            results = model.predict(frame, verbose=False)[0]
            for r in results.boxes.cls.tolist():
                if int(r) == 0:
                    total_people += 1
                else:
                    total_objects += 1
        frame_count += 1
    cap.release()
    return total_people, total_objects, total_people / (total_objects + 1e-6)