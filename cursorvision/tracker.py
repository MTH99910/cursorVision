from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp
import cv2


class FaceTracker:
    def __init__(self, model_path="face_landmarker.task"):
        base_options = python.BaseOptions(model_asset_path=model_path)

        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            num_faces=1,
        )

        self.detector = vision.FaceLandmarker.create_from_options(options)

    def detect(self, frame):
        # OpenCV uses BGR, MediaPipe expects RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to MediaPipe Image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        # Run inference
        results = self.detector.detect(mp_image)

        return results