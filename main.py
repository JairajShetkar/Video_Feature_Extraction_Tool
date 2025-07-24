import json
import sys
from features.shot_cut import detect_shot_cuts
from features.motion_analysis import compute_motion
from features.ocr_text import text_ratio
from features.object_person import person_object_ratio

def convert_types(data):
    # Recursively convert all NumPy types to native Python types
    if isinstance(data, dict):
        return {k: convert_types(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_types(v) for v in data]
    elif hasattr(data, 'item'):
        return data.item()  # Convert numpy types
    else:
        return data

def analyze_video(video_path):
    features = {
        "shot_cut_count": detect_shot_cuts(video_path),
        "average_motion": compute_motion(video_path),
        "text_present_ratio": text_ratio(video_path),
    }
    people, objects, ratio = person_object_ratio(video_path)
    features.update({
        "person_count": people,
        "object_count": objects,
        "person_to_object_ratio": ratio
    })

    return convert_types(features)

if __name__ == "__main__":
    video_path = sys.argv[1]
    features = analyze_video(video_path)
    print(json.dumps(features, indent=2))
