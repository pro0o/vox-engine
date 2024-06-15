import pygame as pg
import moderngl as mg

class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.texture_0 = self.load('test.png')

        self.texture_0.use(location=0)

    
    def load(self, file_name):
        texture = pg.image.load(f'assets/{file_name}')
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        # texture object on the GPU side
        texture =  self.ctx.texture(
            size=texture.get_size(),
            components=4,
            data=pg.image.tostring(texture, 'RGBA', False)
        )

        # TODO: no idea what these actually do, need to study aboutit
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mg.NEAREST, mg.NEAREST)
        return texture

        