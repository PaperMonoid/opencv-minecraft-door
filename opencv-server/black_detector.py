import cv2
import numpy as np


class BlackDetector:
    def __init__(self, blurred, count):
        self.blurred = blurred

        thresholded = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)[1]
        thresholded = cv2.erode(thresholded, None, iterations=8)
        thresholded = cv2.dilate(thresholded, None, iterations=4)
        self.thresholded = thresholded

        contours, hierarchy = cv2.findContours(
            thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:count]
        self.contours = sorted(contours, key=cv2.boundingRect)

    def get_contours(self):
        return self.contours

    def draw_blurred(self, image):
        for contour in self.contours:
            x, y, w, h = cv2.boundingRect(contour)
            blurred = cv2.cvtColor(self.blurred, cv2.COLOR_GRAY2RGB)
            image[y : y + h, x : x + w] = blurred[y : y + h, x : x + w]

    def draw_thresholded(self, image):
        for contour in self.contours:
            x, y, w, h = cv2.boundingRect(contour)
            thresholded = cv2.cvtColor(self.thresholded, cv2.COLOR_GRAY2RGB)
            image[y : y + h, x : x + w] = thresholded[y : y + h, x : x + w]

    def draw(self, image):
        cv2.drawContours(image, self.contours, -1, (30, 255, 30), 2)

        for contour in self.contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (30, 30, 255), 2)
            cv2.putText(
                image,
                "({0},{1})".format(x, y),
                (x, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (30, 30, 255),
                2,
            )
