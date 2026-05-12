import torch
import cv2
import numpy as np
import pathlib

# THE WINDOWS TRANSLATOR FIX
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# 1. Load your custom brain (best.pt)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

model.conf = 0.4  # It shows a box if it is at least 40% sure!


cap = cv2.VideoCapture(0)
print("Starting Final Webcam... Press 'q' to quit!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 2. Convert camera colors (BGR) to AI colors (RGB)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 3. Feed the frame to the AI
    results = model(img, size=416)
    
    # 4. Draw the boxes and convert back to BGR
    rendered_frame = np.squeeze(results.render())
    rendered_frame = cv2.cvtColor(rendered_frame, cv2.COLOR_RGB2BGR)
    
    # 5. Show the live feed
    cv2.imshow('Angelin ASL Detector', rendered_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()