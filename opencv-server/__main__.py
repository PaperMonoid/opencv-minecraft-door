import cv2
import numpy as np

from camera import Camera
from black_detector import BlackDetector
from frequency_detector import FrequencyDetector

import socket
import time

TCP_IP = "localhost"
TCP_PORT = 1069
BUFFER_SIZE = 1

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(1)

print("Waiting on connection...")

connection, address = tcp_socket.accept()

print("Connection accepted!")

detectors = [FrequencyDetector(16), FrequencyDetector(16), FrequencyDetector(16)]
camera = Camera(0.90)

print(detectors[0].frequencies)

for image in camera:
    flipped = cv2.flip(image, 1)
    grayscaled = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayscaled, (11, 11), 0)

    black_detector = BlackDetector(blurred, 3)
    black_contours = black_detector.get_contours()
    any_detected = False
    for detector, black_contour in zip(detectors, black_contours):
        detector.detect(black_detector.thresholded, black_contour)
        any_detected |= detector.draw(flipped, black_contour)

    black_detector.draw(flipped)
    camera.draw(flipped)
    cv2.imshow("Webcam", flipped)

    if any_detected:
        connection.send("1".encode("utf-8"))
    else:
        connection.send("0".encode("utf-8"))

connection.close()
cv2.destroyAllWindows()
