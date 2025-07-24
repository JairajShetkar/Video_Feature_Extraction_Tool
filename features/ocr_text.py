import cv2
import pytesseract

def text_ratio(video_path, sample_rate=30):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    text_frames = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % sample_rate == 0:
            text = pytesseract.image_to_string(frame)
            if len(text.strip()) > 10:
                text_frames += 1
        frame_count += 1
    cap.release()
    return text_frames / (frame_count // sample_rate + 1e-6)