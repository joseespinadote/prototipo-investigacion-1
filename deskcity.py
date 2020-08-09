from ursina import *
import random
import os, stat
import datetime

VELOCIDAD_MOV = 20
lst_entradas = []
edificios = []

with os.scandir(os.environ['USERPROFILE']) as dir_entries:
    for entry in dir_entries:
        if entry.stat().st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN :
            continue
        lst_entradas.append(entry)

def detalle_edificio() :
    Text.size = 0.05
    Text.default_resolution = 1080 * Text.size
    info = Text(text="A powerful waterfall roaring on the mountains")
    info.x = -0.5
    info.y = 0.4
    info.background = True
    info.visible = False

def update():
    if mouse.hovered_entity :
        pass #print(mouse.hovered_entity)

    if held_keys['s']:
        camera.position -= (0, time.dt, 0)
    if held_keys['w']:
        camera.position += (0, time.dt, 0)
    if held_keys['r']:
        camera.position += (0, 0, time.dt)
    if held_keys['f']:
        camera.position -= (0, 0, time.dt)
    if held_keys['a']:
        camera.position -= (time.dt, 0, 0)
    if held_keys['d']:
        camera.position += (time.dt, 0, 0)

    if held_keys['left arrow']:
        camera.rotation_y -= time.dt * VELOCIDAD_MOV
    if held_keys['right arrow']:
        camera.rotation_y += time.dt * VELOCIDAD_MOV
    if held_keys['up arrow']:
        camera.rotation_x -= time.dt * VELOCIDAD_MOV
    if held_keys['down arrow']:
        camera.rotation_x += time.dt * VELOCIDAD_MOV
    if held_keys['z']:
        camera.rotation_z -= time.dt * VELOCIDAD_MOV
    if held_keys['x']:
        camera.rotation_z += time.dt * VELOCIDAD_MOV
app = Ursina()

window.title = 'Prototipo DeskCity (v0.1)'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False

pos_x = 0
pos_y = 0
for entrada in lst_entradas :
    tamanio = entrada.stat().st_size
    if tamanio > 10 :
        tamanio = math.log(entrada.stat().st_size,10)
    cubo_actual = None
    if entrada.is_dir() :
        cubo_actual = Entity(model='cube', color=color.red, scale=(1,1,tamanio), position=(pos_x, pos_y, -tamanio/2), collider="box", texture = 'white_cube')
    else :
        cubo_actual = Entity(model='cube', color=color.blue, scale=(1,1,tamanio), position=(pos_x, pos_y, -tamanio/2) , collider="box", texture = 'white_cube')
    text = Text(parent=cubo_actual, text=entrada.name, wordwrap=10, position=(-0.2,0,-1+tamanio/12), background=True, scale=4)
    edificios.append(cubo_actual)
    pos_x += 1
    if pos_x > 10 :
        pos_x = 0
        pos_y += 1
    if pos_y > 10 :
        break
#bg = Entity(parent=scene, model='quad', texture='shore', scale=(16,8), z=10, color=color.light_gray)
bg = Entity(parent=scene, model='quad', texture='landscape', origin=(-0.25,-0.01), z=0, scale=(15,15))
app.run()
