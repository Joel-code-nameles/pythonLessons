from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Load block texture
grass_texture = load_texture('assets/grass.png')
stone_texture = load_texture('assets/stone.png')
brick_texture = load_texture('assets/brick.png')
dirt_texture = load_texture('assets/dirt.png')
sky_texture = load_texture('assets/skybox.png')

block_pick = 1

# Define the block
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=choose_texture())
            if key == 'right mouse down':
                destroy(self)

# Choose texture based on number keys
def choose_texture():
    if block_pick == 1:
        return grass_texture
    elif block_pick == 2:
        return stone_texture
    elif block_pick == 3:
        return brick_texture
    elif block_pick == 4:
        return dirt_texture

# Create ground
for z in range(10):
    for x in range(10):
        Voxel(position=(x,0,z))

# Skybox
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )

sky = Sky()
player = FirstPersonController()
player.gravity = 0.5

# Handle key input
def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

app.run()
