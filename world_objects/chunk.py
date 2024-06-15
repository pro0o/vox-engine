from settings import *
from meshes.chunk_mesh import ChunkMesh

class Chunk:
    def __init__(self, world, position):
        self.app = world.app
        self.world = world
        self.position = position 

        self.m_model = self.get_model_matrix()
        # array of voxels
        self.voxels: np.array = None
        self.mesh: ChunkMesh = None

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position)* CHUNK_SIZE)
        return m_model
    
    def set_uniform(self):
        self.mesh.program['m_model'].write(self.m_model)

    def build_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        self.set_uniform()
        self.mesh.render()

    def build_voxels(self):
        # initially the voxels will be empty space i.e. 0 in the range of [0-255]
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        # determining the world coordinatees relative to voxel
        cx, cy, cz = glm.ivec3(self.position) * CHUNK_SIZE

        # we use 1d array instead of 3d array, for performance boost
        # so 3d to 1d conversion = x + size*z + area*y

        # filling the chunk with different voxel ranges/
        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                wx = x + cx
                wz = z + cz

                # maybe height of terrain??
                world_height = int(glm.simplex(glm.vec2(wx, wz) * 0.01) * 32 + 32)
                local_height = min(world_height - cy, CHUNK_SIZE) # for current chunk

                for y in range(local_height):
                    wy = y + cy
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = wy + 1
        
        return voxels