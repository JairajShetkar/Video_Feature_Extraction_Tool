import cv2

def compute_motion(video_path):
    cap = cv2.VideoCapture(video_path)
    _, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    motion_magnitudes = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        motion_magnitudes.append(mag.mean())
        prev_gray = gray

    cap.release()
    return sum(motion_magnitudes) / len(motion_magnitudes)