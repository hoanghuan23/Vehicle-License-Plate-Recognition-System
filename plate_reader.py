import pytesseract
import cv2

# Cấu hình pytesseract (đường dẫn tới tesseract.exe)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def read_plate(image):
    """
    Đọc nội dung biển số từ hình ảnh.
    :param image: Ảnh biển số cần nhận diện (NumPy array)
    :return: Nội dung biển số (string)
    """
    try:
        # Chuyển sang grayscale để cải thiện OCR
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Tiền xử lý ảnh (làm mịn)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # Sử dụng pytesseract để nhận diện
        plate_text = pytesseract.image_to_string(gray, config='--psm 7')  # PSM 7: Single line
        return plate_text.strip()
    except Exception as e:
        print(f"Lỗi khi đọc biển số: {e}")
        return ""
