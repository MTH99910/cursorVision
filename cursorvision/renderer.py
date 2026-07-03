import cv2


class Renderer:

    def draw_landmarks(self, frame, state):

        if not state.detected:
            return frame

        height, width, _ = frame.shape

        for landmark in state.landmarks:

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            cv2.circle(
                frame,
                (x, y),
                1,
                (0, 255, 0),
                -1
            )

        return frame