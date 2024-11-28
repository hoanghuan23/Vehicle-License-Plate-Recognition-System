from ultralytics import YOLO

# Kiểm tra YOLO và camera
model = YOLO('yolov8m.pt')

try:
    results = model.predict(source=0, show=True, save_txt=True, save_conf=True, save_crop=True)

except Exception as e:
    print("Lỗi xảy ra:", e)
