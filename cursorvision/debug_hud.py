import cv2


class DebugHUD:

    def draw(self, frame, state):

        lines = [
            f"Detected : {state.detected}",
            f"Yaw      : {state.yaw:.2f}",
            f"Pitch    : {state.pitch:.2f}",
            f"Roll     : {state.roll:.2f}",
        ]

        x = 15
        y = 30

        for line in lines:

            cv2.putText(
                frame,
                line,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )

            y += 25

        return frame