import cv2

def detect_shot_cuts(video_path, threshold=0.5):
    cap = cv2.VideoCapture(video_path)
    prev_hist = None
    cuts = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hist = cv2.calcHist([cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        if prev_hist is not None:
            diff = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA)
            if diff > threshold:
                cuts += 1
        prev_hist = hist
    cap.release()
    return cuts