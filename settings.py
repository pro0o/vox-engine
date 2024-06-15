from numba import njit
import numpy as np
import glm
import math

# the context resolution
WIN_RES = glm.vec2(800, 600)

BG_COLOR = glm.vec3(0.1, 0.16, 0.25)

# chunkz
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

# world
WORLD_W, WORLD_H = 4, 3
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_H
WORLD_V = WORLD_H * WORLD_D * WORLD_W

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE


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
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENS = 0.002

