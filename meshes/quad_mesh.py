from settings import *
from meshes.base_mesh import BaseMesh

class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.quad

        self.format = '3f 3f'
        self.attrs = ('in_position', 'in_color')
        self.vao = self.get_vao()

    # vertex data for the quad
    def get_vertex_data(self):
        # two triangles in counter clockwise direction for opengl
        vertices = [
            (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0)
        ]

        colors = [
            (0, 1, 0), (1, 0, 0), (1, 1, 0),
            (0, 1,0), (1, 1, 0), (0, 0, 1)
        ]

        vertex_data = np.hstack([vertices, colors], dtype='float32')
        return vertex_data


        