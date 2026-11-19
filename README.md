# Heat / Fire Detection

Python prototype that watches a camera feed for flame-coloured regions and sounds a spoken alarm.

## Done so far

- Fire detection (`detect_fire`) by converting each frame to HSV and masking flame-like colour ranges with OpenCV
- Spoken alarm (`trigger_alarm`) using pyttsx3 text-to-speech
- A YOLOv8 nano weights file (`yolov8n.pt`) is included for the planned model-based version

## Stack

Python, OpenCV, NumPy, pyttsx3

## Run locally

```bash
pip install opencv-python numpy pyttsx3
python main.py
```

## Limitations

Colour thresholding can fire on any red or orange object, so false alarms are likely. `main.py` does not use the YOLO weights yet.

## Future scope

- Replace colour masking with a YOLOv8 model trained on fire and smoke data
- Add temporal checks (flicker and motion) to cut false positives
- Send alerts by SMS, email or webhook, and log events with snapshots
- Support multiple cameras and RTSP streams
- Report detection accuracy on a labelled test set
