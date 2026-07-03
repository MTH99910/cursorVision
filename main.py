from cursorvision.camera import Camera
from cursorvision.tracker import FaceTracker
from cursorvision.renderer import Renderer
import cv2


def main():
    camera = Camera()

    tracker = FaceTracker()

    renderer = Renderer()

    print("FaceTracker loaded successfully!")

    while True:
        success, frame = camera.read()

        if not success:
            break

        state = tracker.detect(frame)

        frame = renderer.draw_landmarks(frame, state)

        cv2.imshow("CursorVision", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()