from cursorvision.camera import Camera
from cursorvision.tracker import FaceTracker
import cv2


def main():
    camera = Camera()

    tracker = FaceTracker()

    print("FaceTracker loaded successfully!")

    while True:
        success, frame = camera.read()

        if not success:
            break

        cv2.imshow("CursorVision", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()