import cv2
import time
import numpy as np


class Camera:
    def __init__(self, sample_rate):
        self.camera = cv2.VideoCapture(0)
        self.sample_rate = sample_rate
        self.sample_rates = np.zeros((5,), dtype="float")

    def framerate(self):
        return np.average(self.sample_rates)

    def __iter__(self):
        i = 0
        time_start = time.time()
        while True:
            value, image = self.camera.read()

            if cv2.waitKey(1) == 27:  # esc to quit
                break

            time_now = time.time()
            time_difference = time_now - time_start

            if time_difference > self.sample_rate:
                time_start = time_now

                self.sample_rates[i] = time_difference
                if i < 4:
                    i += 1
                else:
                    i = 0

                yield image

    def draw(self, image):
        cv2.putText(
            image,
            "FPS: {0:.2f}".format(1 / self.framerate()),
            (30, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.80,
            (30, 30, 255),
            3,
        )
