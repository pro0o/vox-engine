import numpy as np

class BaseMesh:
    def __init__(self):
        self.ctx = None
        # shaders program
        self.program = None

        # type of vertex object [format: 3f 3f]
        self.format = None

        # attribute of object [format: in_position, in_color]
        self.attrs: tuple[str, ...] = None

        # vertex array object
        self.vao = None

    ##these are input to the shader program
    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.format, *self.attrs)], skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()