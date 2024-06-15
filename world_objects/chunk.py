from settings import *
from meshes.chunk_mesh import ChunkMesh
import logging

logger = logging.getLogger(__name__)

class Chunk:
    def __init__(self, world, position):
        self.app = world.app
        self.world = world
        self.position = position 
        self.m_model = self.get_model_matrix()
        self.voxels = None
        self.mesh = None
        self.is_empty = True

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position) * CHUNK_SIZE)
        return m_model
    
    def set_uniform(self):
        if self.mesh and self.mesh.program:
            self.mesh.program['m_model'].write(self.m_model)
        else:
            logger.error(f"Mesh or program not initialized for chunk at {self.position}")

    def build_mesh(self):
        if not self.is_empty:
            self.mesh = ChunkMesh(self)
            if self.mesh:
                logger.debug(f"Mesh built for chunk at position {self.position}")
            else:
                logger.error(f"Failed to build mesh for chunk at position {self.position}")
        else:
            logger.debug(f"Skipping mesh build for empty chunk at position {self.position}")

    def render(self):
        if not self.is_empty and self.mesh:
            self.set_uniform()
            self.mesh.render()
        else:
            logger.debug(f"Skipping render for empty chunk or chunk without mesh at position {self.position}")

    def build_voxels(self):
        # initially the voxels will be empty space i.e. 0 in the range of [0-255]
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        # determining the world coordinatees relative to voxel
        cx, cy, cz = glm.ivec3(self.position) * CHUNK_SIZE

        # we use 1d array instead of 3d array, for performance boost
        # so 3d to 1d conversion = x + size*z + area*y

        # filling the chunk with different voxel ranges/
        for x in range(CHUNK_SIZE):
            wx = x + cx
            for z in range(CHUNK_SIZE):
                wz = z + cz
                world_height = int(glm.simplex(glm.vec2(wx, wz) * 0.01) * 32 + 32)
                local_height = min(world_height - cy, CHUNK_SIZE)

                for y in range(local_height):
                    wy = y + cy
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = wy + 1

        self.is_empty = not np.any(voxels)
        logger.debug(f"Voxels built for chunk at position {self.position}, empty: {self.is_empty}")
        return voxels
