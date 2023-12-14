from variaveis import *

boss_vida = 150
boss_velocidade = 165

#------BOSS-FRAMES------#
boss_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle.png", 6)
boss_direita = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle2.png",6)
boss_atacando_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_attack/demon-attack.png",11)
boss_atacando_direita = Sprite("Game Assets/Mobs/Final Boss/boss_attack/demon-attack2.png",11)
boss_direita.set_total_duration(750)
boss_esquerda.set_total_duration(750)
boss_atacando_direita.set_total_duration(1000)
boss_atacando_esquerda.set_total_duration(1000)
boss_hitbox = Sprite("Game Assets/Mobs/Final Boss/boss_idle/boss_hitbox.png")
boss_hitbox_ataque_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_attack/boss_attack_hitbox.png")
boss_hitbox_ataque_direita = Sprite("Game Assets/Mobs/Final Boss/boss_attack/boss_attack_hitbox2.png")
boss_direction = [-1]

#------ATAQUE-BOSS------#
boss_intervalo_ataque_cronometro = 0
boss_atacando_cronometro = 0
boss_atacando = False
boss_dano_fogo = 10

def boss_hitbox_accuracy():
    boss_hitbox.x = boss_esquerda.x
    boss_hitbox.y = boss_esquerda.y
    boss_hitbox_ataque_esquerda.x = (boss_esquerda.x - 50)
    boss_hitbox_ataque_esquerda.y = boss_esquerda.y
    boss_hitbox_ataque_direita.x = boss_esquerda.x + 25
    boss_hitbox_ataque_direita.y = boss_esquerda.y - 10

def boss_direction_now ():
    if (boss_hitbox.x) > (player.x):
        boss_direction[0] = -1
    if (boss_hitbox.x + boss_hitbox.width) < player.x:
        boss_direction[0] = 1

def boss_move (boss_atacando):
    if (not boss_atacando):
        if (boss_hitbox.x) > (player.x):
            boss_direction[0] = -1
            boss_esquerda.x -= boss_velocidade * janela.delta_time()
        if (boss_hitbox.x + boss_hitbox.width) < player.x:
            boss_direction[0] = 1
            boss_esquerda.x += boss_velocidade * janela.delta_time()

def boss_draw(boss_atacando):
    if (boss_direction[0] == -1):
        if (not boss_atacando):
            boss_esquerda.draw()
            boss_esquerda.update()
        else:
            boss_atacando_esquerda.draw()
            boss_atacando_esquerda.update()
    if (boss_direction[0] == 1):
        if (not boss_atacando):
            boss_direita.draw()
            boss_direita.update()
        else:
            boss_atacando_direita.draw()
            boss_atacando_direita.update()

def boss_sincronismo ():
    boss_direita.x = boss_esquerda.x
    boss_direita.y = boss_esquerda.y
    boss_atacando_esquerda.x = boss_esquerda.x - 45
    boss_atacando_esquerda.y = boss_esquerda.y - 35
    boss_atacando_direita.x = boss_esquerda.x - 25
    boss_atacando_direita.y = boss_esquerda.y - 35