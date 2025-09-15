import cv2
import pytesseract

# --- set tesseract path (only needed on Windows) ---
# Example path, adjust if installed elsewhere:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- load the image ---
image_path = "your_image.jpg"   # replace with your image file
img = cv2.imread(image_path)

# --- preprocess (convert to grayscale + optional thresholding) ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# --- extract text ---
extracted_text = pytesseract.image_to_string(gray)

print("Extracted Text:\n", extracted_text)
