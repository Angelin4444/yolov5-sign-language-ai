# Sign Language Detection using YOLOv5

<p align="center">
<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/65933e20-b5f6-4a00-b31a-d8f79903b664" /> <br>
<img width="1664" height="1664" alt="train_batch0" src="https://github.com/user-attachments/assets/9c4b869c-8e7f-4cfb-a9d3-29d8b678b9b2" /> </p>

## Overview
This project is a real-time sign language detection system built using YOLOv5. It detects hand gestures and translates them into predefined labels to support communication accessibility.

## Objective
The aim of this project is to explore how computer vision and machine learning can be used to bridge communication gaps between hearing and non-hearing individuals.

## Technologies Used
- Python
- YOLOv5 (Object Detection Model)
- Google Colab
- OpenCV
- Visual Studio Code

## Dataset
A custom dataset was created using webcam image capture. Each gesture was manually collected and annotated.

- 23 labels/classes
- 100 images per class
- Approximately 2300 annotated images

## Model Training
The YOLOv5 model was trained using Google Colab with GPU support. Training graphs showed high performance with approximately 99% accuracy.

## Features
- Real-time webcam detection
- Custom-trained sign language recognition
- High accuracy prediction on trained dataset

## Results
The model successfully detects hand gestures in real-time with strong accuracy under controlled lighting conditions.

## Future Improvements
- Increase dataset size
- Improve performance in different lighting conditions
- Add more sign language gestures
- Deploy as a web or mobile application

## Note
This project was developed as part of a university assignment for the Emerging Technologies module.

## Author
Developed as part of an Emerging Technologies module.
