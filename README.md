# Video_Feature_Extraction_Tool

## 📌 Overview
This Python tool extracts visual and temporal features from a local video file using OpenCV, Tesseract OCR, and YOLO.

## ✅ Features Implemented
- Shot Cut Detection
- Motion Analysis (Optical Flow)
- Text Detection (OCR)
- Object vs. Person Dominance using YOLO

## Below are the steps to run the file locally:

## Step1: Download the files in zip format and extract.

#### Note:- Ensure Python 3.8+ version is installed on the computer
## Step2: Run the requirements.txt file
```cmd 
pip install -r requirements.txt
```

## Step3: Install Tesseract OCR:
- Windows: https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md

## Step4: Run the below command to run the tool
```cmd
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
