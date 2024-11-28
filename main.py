from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8m.pt")

# train the model
results = model.train(data='config.yaml', epochs = 3)