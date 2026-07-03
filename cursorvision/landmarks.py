from enum import IntEnum


class FaceLandmark(IntEnum):

    # Nose
    NOSE_TIP = 1

    # Left eye
    LEFT_EYE_OUTER = 33
    LEFT_EYE_INNER = 133
    LEFT_EYE_TOP = 159
    LEFT_EYE_BOTTOM = 145

    # Right eye
    RIGHT_EYE_OUTER = 263
    RIGHT_EYE_INNER = 362
    RIGHT_EYE_TOP = 386
    RIGHT_EYE_BOTTOM = 374

    # Left iris
    LEFT_IRIS_CENTER = 468

    # Right iris
    RIGHT_IRIS_CENTER = 473

    # Mouth
    MOUTH_LEFT = 61
    MOUTH_RIGHT = 291
    UPPER_LIP = 13
    LOWER_LIP = 14

    # Chin
    CHIN = 152