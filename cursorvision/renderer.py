import cv2
from cursorvision.landmarks import FaceLandmark

class Renderer:

    def landmark_to_pixel(self, landmark, width, height):

        x = int(landmark.x * width)
        y = int(landmark.y * height)

        return x, y 

    def draw_landmarks(self, frame, state):

        if not state.detected:
            return frame

        height, width, _ = frame.shape

        for landmark in state.landmarks:

            x, y = self.landmark_to_pixel(
                landmark,
                width,
                height
            )

            cv2.circle(
                frame,
                (x, y),
                1,
                (0, 255, 0),
                -1
            )

        left_iris = state.get_landmark(FaceLandmark.LEFT_IRIS_CENTER)
        right_iris = state.get_landmark(FaceLandmark.RIGHT_IRIS_CENTER)

        x, y = self.landmark_to_pixel(left_iris, width, height)

        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

        x, y = self.landmark_to_pixel(right_iris, width, height)

        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

        return frame