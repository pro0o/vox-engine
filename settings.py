from numba import njit
import numpy as np
import glm
import math

# the context resolution
WIN_RES = glm.vec2(800, 600)

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y

# fiend of view 
# aka view frustum 
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.2
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player 
PLAYER_SPEED = 0.007
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENS = 0.002

# bg color
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)

