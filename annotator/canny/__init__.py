import cv2

class CannyDetector:
    def __call__(self, img, low_threshold, high_threshold):
        return cv2.Canny(img, low_threshold, high_threshold)

def apply_canny(img, low_threshold, high_threshold):
    # This wrapper function makes the class compatible with your model.py
    return CannyDetector()(img, low_threshold, high_threshold)