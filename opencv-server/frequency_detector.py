import cv2
import numpy as np


class FrequencyDetector:
    def __init__(self, samples):
        self.samples = samples
        self.data = [128] * self.samples
        self.frequencies = np.fft.fftfreq(self.samples)
        self.result = []

    def detect(self, image, contour):
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y : y + h, x : x + w]
        self.data.append(np.average(roi))
        self.data = self.data[-self.samples :]

        self.result = np.fft.fft(self.data)

    def draw(self, image, contour):
        data = sorted(
            zip(self.frequencies, self.result), key=lambda x: x[1], reverse=True
        )

        color = (255, 30, 30)
        count = 0
        for (frequency, result) in data[1:5]:
            count += abs(0.125 - abs(frequency)) <= 0.05 and result >= 10
            count += abs(0.25 - abs(frequency)) <= 0.05 and result >= 10

        if count >= 4:
            print(data[1:5])
            color = (30, 255, 30)

        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(
            image,
            "{0:.2f} {1:.2f} {2:.2f} {3:.2f}".format(
                data[1][0], data[2][0], data[3][0], data[4][0]
            ),
            (x, y - 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            color,
            2,
        )
