import cv2
import numpy as np

from camera import Camera
from black_detector import BlackDetector
from frequency_detector import FrequencyDetector

detectors = [FrequencyDetector(16), FrequencyDetector(16), FrequencyDetector(16)]
camera = Camera(0.90)

print(detectors[0].frequencies)

for image in camera:
    flipped = cv2.flip(image, 1)
    grayscaled = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayscaled, (11, 11), 0)

    black_detector = BlackDetector(blurred, 3)
    black_contours = black_detector.get_contours()
    for detector, black_contour in zip(detectors, black_contours):
        detector.detect(black_detector.thresholded, black_contour)
        detector.draw(flipped, black_contour)

    black_detector.draw(flipped)
    camera.draw(flipped)
    cv2.imshow("Webcam", flipped)


cv2.destroyAllWindows()
