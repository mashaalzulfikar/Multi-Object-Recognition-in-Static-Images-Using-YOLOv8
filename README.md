# Multi-Object Recognition in Static Images Using YOLOv8

## Introduction
This project implements a multi-object recognition system using the YOLOv8 (You Only Look Once) architecture. Object detection is a critical component of computer vision, enabling the identification and localization of objects within images for applications such as surveillance, autonomous driving, and image retrieval. This project provides a step-by-step implementation for detecting multiple objects in static images with high speed and accuracy.

## Features
- **YOLOv8 Integration**: Utilizes the latest YOLOv8 model for real-time inference.
- **Web Interface**: A Flask-based web application allowing users to upload images and view detection results.
- **Automated Processing**: Efficiently identifies bounding boxes and class probabilities for various objects.

## Project Structure
```text
├── app.py              # Main Flask application logic
├── requirements.txt    # Project dependencies
├── templates/          # HTML templates for the web interface
│   ├── index.html      # Image upload page
│   └── result.html     # Detection results display page
└── uploads/            # Temporary storage for uploaded images
    └── .gitkeep        # Placeholder to ensure folder is tracked
```

## Prerequisites
To run this project, ensure you have Python installed. Install the necessary dependencies via terminal:

```bash
pip install -r requirements.txt

```

## How to Run
1. Navigate to the project directory.
2. Start the application by running:

```bash
python app.py

```
3. Open your web browser and go to `http://127.0.0.1:5000`.
4. Upload an image, and the system will display the detected objects.

## Methodology
The project follows these core steps:
1. **Load Model**: Utilizes the pre-trained `yolov8n.pt` model for initial detection.
2. **Preprocessing**: Handles user-uploaded images and prepares them for inference.
3. **Inference**: The YOLOv8 model processes the image to identify objects.
4. **Output**: Displays bounding box data and class labels to the user.
