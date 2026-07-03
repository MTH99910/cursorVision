import cv2


class Renderer:

    def draw_landmarks(self, frame, results):

        if not results.face_landmarks:
            return frame

        height, width, _ = frame.shape

        for face in results.face_landmarks:

            for landmark in face:

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