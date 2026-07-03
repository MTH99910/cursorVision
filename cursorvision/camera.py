import cv2


class Camera:
    def __init__(self, camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam.")

    def read(self):
        success, frame = self.cap.read()

        if not success:
            return None

        success, frame = self.cap.read()
        return success, frame

    def release(self):
        self.cap.release()
