import cv2
import numpy as np

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def process_image(img, rect_start, rect_end):
    try:
        if rect_start and rect_end:
            x1, y1 = rect_start
            x2, y2 = rect_end

            # Ensure coordinates are in the correct order
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)

            # Dim the entire image
            dimmed_img = (img * 0.75).astype(np.uint8)

            # Extract ROI and perform histogram equalization
            roi = img[y1:y2, x1:x2]
            equalized_roi = cv2.equalizeHist(roi)

            # Insert the equalized ROI back into the dimmed image
            dimmed_img[y1:y2, x1:x2] = equalized_roi

            # Display the final image
            cv2.imshow('Image', dimmed_img)
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")