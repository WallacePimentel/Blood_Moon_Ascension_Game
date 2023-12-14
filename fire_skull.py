from variaveis import *
import random

#------VARIAVEIS-DE-SPAWN-E-MOVIMENTAÇAO------#
numero = 5
lista_skull_right = []
lista_skull_left = []
lista_skull_up = []
velocidade_skull = 800
skull_plus = 200
skull_plus_up = 100
skull_left_moved = False
contador_passadas = [0]

#------VARIAVEIS-DE-ANIMAÇÃO------#
skull_dano = 20

def skull_spawn_left ():
    for i in range(numero):
        new_skull = Sprite("Game Assets/Mobs/Fire Skull/skull_right/fire-skull2.png",8)
        new_skull.set_total_duration(1000)
        new_skull.set_position(-1200 + skull_plus * i,janela.height - new_skull.height - 20 - (200 * i * 0.5 ))
        lista_skull_left.append(new_skull)

def skull_spawn_right ():
    for i in range(numero):
        new_skull = Sprite("Game Assets/Mobs/Fire Skull/skull_left/fire-skull.png",8)
        new_skull.set_total_duration(1000)
        new_skull.set_position(janela.width + 2400 - skull_plus * i,janela.height - new_skull.height - 20 - (200 * i * 0.5 ))
        lista_skull_right.append(new_skull)

def skull_spawn_up ():
    for i in range(numero):
        new_skull = Sprite("Game Assets/Mobs/Fire Skull/skull_up/fire-skull3.png",8)
        new_skull.set_total_duration(1000)
        new_skull.set_position(30 + (skull_plus * (random.randint(0,7))) + (skull_plus * i),-1200)
        lista_skull_up.append(new_skull)

def skull_draw():
    for i in range(numero):
        lista_skull_left[i].draw()
        lista_skull_right[i].draw()
        lista_skull_left[i].update()
        lista_skull_right[i].update()
        lista_skull_up[i].draw()
        lista_skull_up[i].update()

def skull_move_left ():
    if (onda < 3):
        for i in range(numero):
            lista_skull_left[i].x += velocidade_skull * janela.delta_time()
            if (lista_skull_left[i].x >= janela.width):
                lista_skull_left[i].set_position(-1200,lista_skull_left[i].y)

def skull_move_right():
    if (onda < 3):
        for i in range(numero):
            lista_skull_right[i].x -= velocidade_skull * janela.delta_time()
            if (lista_skull_right[i].x <= 0):
                lista_skull_right[i].set_position(janela.width + 2400, lista_skull_right[i].y)

def skull_move_up ():
    if (onda < 3):
        for i in range(numero):
            lista_skull_up[i].y += velocidade_skull * janela.delta_time()
            if (lista_skull_up[i].y >= janela.height):
                lista_skull_up[i].set_position(30 + (skull_plus * (random.randint(0,7))) + (skull_plus * i),-1200)
                contador_passadas[0] += 1

def fim_skull ():
    if (onda > 2):
        for i in range(numero):
            lista_skull_left[i].set_position(1000000,1000000)
            lista_skull_right[i].set_position(1000000,1000000)
            lista_skull_up[i].set_position(1000000,1000000)