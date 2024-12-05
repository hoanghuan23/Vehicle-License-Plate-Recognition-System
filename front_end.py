import tkinter as tk
from tkinter import filedialog, messagebox
from ultralytics import YOLO
from PIL import Image
import cv2

root = tk.Tk()
root.title("Nhận diện biển số xell")
root.geometry("1000x600")

bg = tk.PhotoImage(file="background.png")
label1 = tk.Label(root, image=bg)
label1.place(relwidth=1, relheight=1)

def process_image(image_path):

    model = YOLO('F:/Python/biensoxe/runs/detect/train6/weights/best.pt')

    # Hiển thị ảnh gốc
    Image.open(image_path).show()

    # Phát hiện biển số
    results = model(image_path)
    for r in results:
        im_array = r.plot()
        labeled_image = Image.fromarray(im_array[..., ::-1])
        labeled_image.show()

    messagebox.showinfo("Processing", f"Đã xử lý ảnh: {image_path}")


def process_video(video_path):
    model_path = 'F:/Python/biensoxe/runs/detect/train6/weights/best.pt'
    output_video_path = video_path.replace('.mp4', '_processed.mp4')

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Error", "Không thể đọc video.")
        return

    H, W, _ = frame.shape

    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

    # Load model
    model = YOLO(model_path)
    threshold = 0.5  # Ngưỡng phát hiện

    while ret:
        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = map(int, result[:4]) + result[4:]
            if score > threshold:
                # Vẽ khung chữ nhật và thêm nhãn
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        out.write(frame)
        ret, frame = cap.read()

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    messagebox.showinfo("Processing", f"Đã xử lý xong video: {output_video_path}")


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        process_image(file_path)


def select_video():

    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    if file_path:
        process_video(file_path)


# Giao diện các nút bấm
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor="center")

btn_image = tk.Button(button_frame, text="Chọn Ảnh", command=select_image, font=("Arial", 18), width=15, height=2)
btn_image.grid(row=0, column=0, padx=10, pady=10)

btn_video = tk.Button(button_frame, text="Chọn Video", command=select_video, font=("Arial", 18), width=15, height=2)
btn_video.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
