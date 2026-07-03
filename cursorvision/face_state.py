from dataclasses import dataclass, field


@dataclass
class FaceState:

    # General
    detected: bool = False

    # Complete landmark list
    landmarks: list = field(default_factory=list)

    # Head rotation

    facial_transform = None

    yaw: float = 0.0
    pitch: float = 0.0
    roll: float = 0.0

    # Eye state
    left_eye_open: float = 0.0
    right_eye_open: float = 0.0

    # Eyebrows
    left_eyebrow_raise: float = 0.0
    right_eyebrow_raise: float = 0.0

    # Gaze
    gaze_x: float = 0.0
    gaze_y: float = 0.0
    def get_landmark(self, landmark):
        return self.landmarks[int(landmark)]