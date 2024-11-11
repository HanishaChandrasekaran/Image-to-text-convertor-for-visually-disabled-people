import cv2

def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy.
    This includes grayscale conversion, thresholding, and denoising.
    """
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, thresh_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY)
    return thresh_image
