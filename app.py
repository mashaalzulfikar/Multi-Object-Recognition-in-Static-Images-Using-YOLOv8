from flask import Flask, request, render_template
from ultralytics import YOLO
import os

app = Flask(__name__)

# Ensure the uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Load the pre-trained YOLOv8 model
# 'yolov8n.pt' will be downloaded automatically by ultralytics on the first run
model = YOLO('yolov8n.pt') 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No file selected", 400
    
    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    # Make predictions
    results = model.predict(file_path)
    
    # Process results
    detections = []
    for result in results:
        # Appending the result object to display in the template
        detections.append(str(result.tojson())) 
        
    return render_template('result.html', detections=detections)

if __name__ == '__main__':
    app.run(debug=True)
