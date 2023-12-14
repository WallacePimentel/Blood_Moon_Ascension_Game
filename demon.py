from variaveis import *

#Demonio
demon = Sprite("Game Assets/Mobs/Demon King/demon_idle/demon_idle_1.png")
demon_morrendo = Sprite("Game Assets/Mobs/Demon King/demon_death/demon_death_1.png")
v_demon = 85


#Animação Demonio
index_animacao_d = 0
index_animacao_death_demonio = 0
demon_w1 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_1.png").convert_alpha(), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_2.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_3.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_4.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_5.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_6.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_7.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_8.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_9.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_10.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_11.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_12.png")]
demon_w2 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_1.png").convert_alpha(),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_12.png")]
demon_at1 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_1.png").convert_alpha(), pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_12.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_13.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_14.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_15.png")]
demon_at2 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_1.png").convert_alpha(),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_12.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_13.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_14.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_15.png")]
demon_dy = [pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_1.png").convert_alpha(),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_12.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_13.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_14.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_15.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_16.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_17.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_18.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_19.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_20.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_21.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_death/demon_death_22.png")]
#Status demonio
cronometro_dano_sofrido_demon = 0
vida_demon = 200
dano_tomado = 0
demon_attacking = False
demon_atacou = False
demon_cronometro = 0
demon_direction = -1
demon_delay_attack = 3
player_levou_dano = False
cronometro_excluir = 0