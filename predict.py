# from ultralytics import YOLO
# from PIL import Image
#
# model = YOLO('F:/Python/biensoxe/runs/detect/train3/weights/best.pt')  # Load model
#
# image_path = 'C:/Users/ACER/Downloads/xemay.jpg'
# # Hiển thị ảnh gốc trước
# original_image = Image.open(image_path)
# original_image.show()
#
# results = model(image_path)
#
# for r in results:
#     print(r.boxes)
#     im_array = r.plot()
#     labeled_image = Image.fromarray(im_array[..., ::-1])
#     labeled_image.show()

# from ultralytics import YOLO
# import cv2
#
# # Đường dẫn tới video và mô hình đã được huấn luyện
# video_path = 'F:/Python/biensoxe/video.mp4'
# model_path = 'F:/Python/biensoxe/runs/detect/train4/weights/best.pt'
# output_video_path = video_path.replace('.mp4', '_new.mp4')
#
# cap = cv2.VideoCapture(video_path)
# ret, frame = cap.read()
# H, W, _ = frame.shape
#
# # Cài đặt VideoWriter để lưu video kết quả
# out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))
#
# # Tải mô hình YOLO đã huấn luyện
# model = YOLO(model_path)
# threshold = 0.5  # Ngưỡng để phát hiện đối tượng
#
# # Số khung hình để duy trì nhãn sau phát hiện
# hold_frames = 5
# last_detection = None
# hold_counter = 0
#
# while ret:
#     # Phát hiện đối tượng trên frame hiện tại
#     results = model(frame)[0]
#     detected = False
#
#     # Duyệt qua tất cả các kết quả phát hiện
#     for result in results.boxes.data.tolist():
#         x1, y1, x2, y2, score, class_id = result
#
#         # Kiểm tra nếu điểm số phát hiện đủ cao
#         if score > threshold:
#             # Lưu vị trí phát hiện vào last_detection và reset hold_counter
#             last_detection = (int(x1), int(y1), int(x2), int(y2))
#             hold_counter = hold_frames
#             detected = True
#             break
#
#     # Nếu không có phát hiện mới, giảm hold_counter
#     if not detected and hold_counter > 0:
#         hold_counter -= 1
#
#     # Nếu có last_detection và hold_counter còn > 0, hiển thị nhãn
#     if last_detection and hold_counter > 0:
#         x1, y1, x2, y2 = last_detection
#         # Vẽ khung chữ nhật xung quanh biển số
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#
#         # Cắt và phóng to vùng biển số
#         license_plate = frame[y1:y2, x1:x2]
#         zoomed_plate = cv2.resize(license_plate, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
#         zoomed_h, zoomed_w, _ = zoomed_plate.shape
#         x_offset = x1
#         y_offset = max(y1 - zoomed_h, 0)  # Đặt phóng to phía trên biển số (cách biển số một khoảng)
#
#         # Kiểm tra và điều chỉnh nếu vượt quá biên video
#         if x_offset + zoomed_w > W:
#             zoomed_w = W - x_offset
#         if y_offset + zoomed_h > H:
#             zoomed_h = H - y_offset
#
#         # Chèn vùng biển số đã phóng to lên frame gốc
#         frame[y_offset:y_offset + zoomed_h, x_offset:x_offset + zoomed_w] = zoomed_plate[:zoomed_h, :zoomed_w]
#
#     # Ghi frame đã xử lý vào video đầu ra
#     out.write(frame)
#     ret, frame = cap.read()
#
# # Giải phóng tài nguyên
# cap.release()
# out.release()
# cv2.destroyAllWindows()


