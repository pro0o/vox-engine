from numba import njit
import numpy as np
import glm
import math

# the context resolution
WIN_RES = glm.vec2(800, 600)

# bg color
BG_COLOR = glm.vec3(1.0, 1.0, 0.0)
