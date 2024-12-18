import cv2
from image_processing import process_image

# Initialize global variables for rectangle drawing
rect_start = None
rect_end = None
drawing = False

# Mouse callback function to draw a rectangle
def draw_rectangle(event, x, y, flags, param):
    global rect_start, rect_end, drawing
    img = param  # The image on which to draw the rectangle

    try:
        if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button pressed
            rect_start = (x, y)  # Set the starting point of the rectangle
            drawing = True  # Start drawing

        elif event == cv2.EVENT_MOUSEMOVE:  # Mouse movement
            if drawing:  # If currently drawing
                rect_end = (x, y)  # Update the ending point of the rectangle
                img_copy = img.copy()  # Create a copy of the image to draw on
                cv2.rectangle(img_copy, rect_start, rect_end, (255, 255, 255), 1)  # Draw the rectangle
                cv2.imshow('Image', img_copy)  # Show the image with the rectangle

        elif event == cv2.EVENT_LBUTTONUP:  # Left mouse button released
            rect_end = (x, y)  # Set the ending point of the rectangle
            drawing = False  # Stop drawing
            process_image(img, rect_start, rect_end)  # Process the selected region of the image
    except Exception as e:
        print(f"An error occurred: {e}")