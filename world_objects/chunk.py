from settings import *
from meshes.chunk_mesh import ChunkMesh

class Chunk:
    def __init__(self, app):
        self.app = app
        # array of voxels
        self.voxels: np.array = self.build_voxels()
        self.mesh: ChunkMesh = None
        self.build_mesh()

    def build_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        self.mesh.render()

    def build_voxels(self):
        # initially the voxels will be empty space i.e. 0 in the range of [0-255]
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        # we use 1d array instead of 3d array, for performance boost
        # so 3d to 1d conversion = x + size*z + area*y

        # filling the chunk with different voxel ranges/
        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                for y in range(CHUNK_SIZE):
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = (
                        # 3d noise with simplex func
                        x + y + z if int(glm.simplex(glm.vec3(x,y,z) * 0.1)+1) else 0
                    )
        return voxels