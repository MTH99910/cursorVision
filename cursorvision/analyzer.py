import time
from scipy.spatial.transform import Rotation as R

# Verified experimentally on 2026-07-03
# YXZ order gives intuitive head motion:
#   yaw   -> turn left/right
#   pitch -> nod up/down
#   roll  -> tilt head
EULER_ORDER = "yxz"

class Analyzer:

    def __init__(self):
        self.last_print = 0


    def analyze(self, state):

        if not state.detected:
            return state

        if state.facial_transform is not None:

            now = time.time()

            if now - self.last_print > 1:

                self.last_print = now

                print(state.facial_transform)
        
        matrix = state.facial_transform[:3, :3]

        rotation = R.from_matrix(matrix)

        angles = rotation.as_euler(
            EULER_ORDER,
            degrees=True
        )

        state.yaw = angles[0]
        state.pitch = angles[1]
        state.roll = angles[2]

        return state