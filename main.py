# Hayden Berberich
# 12-2-2024

import cv2
import argparse
from mouse_callbacks import draw_rectangle
from image_processing import load_image

def main(image_path):
    try:
        # Load the grayscale image
        img = load_image(image_path)

        # Create a window and set the mouse callback function
        cv2.namedWindow('Image')
        cv2.setMouseCallback('Image', draw_rectangle, img)

        # Display the image
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process an image.')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()
    main(args.image_path)