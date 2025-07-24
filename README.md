# Video_Feature_Extraction_Tool

## 📌 Overview
This Python tool extracts visual and temporal features from a local video file using OpenCV, Tesseract OCR, and YOLO.

## ✅ Features Implemented
- Shot Cut Detection
- Motion Analysis (Optical Flow)
- Text Detection (OCR)
- Object vs. Person Dominance using YOLO

## 📦 Requirements
```terminal 
pip install opencv-python pytesseract numpy torch torchvision torchaudio ultralytics
```

Install Tesseract OCR:
- Windows: https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md

## 🚀 Usage
```bash
python main.py test_videos/sample.mp4
```

## 🧪 Sample Output
```json
{
  "shot_cut_count": 12,
  "average_motion": 0.348,
  "text_present_ratio": 0.23,
  "person_count": 58,
  "object_count": 80,
  "person_to_object_ratio": 0.725
}
