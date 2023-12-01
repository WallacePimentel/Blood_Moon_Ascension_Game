from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *
from variaveis import *

#Demonio
demon = Sprite("Game Assets/Mobs/Demon King/demon_idle/demon_idle_1.png")
v_demon = 65

#Animação Demonio
index_animacao_d = 0
demon_w1 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_1.png").convert_alpha(), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_2.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_3.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_4.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_5.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_6.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_7.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_8.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_9.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_10.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_11.png"), pygame.image.load("Game Assets/Mobs/Demon King/demon_walk/demon_walk_12.png")]
demon_w2 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_1.png").convert_alpha(),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_walk_left/demon_walk_12.png")]
demon_at1 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_1.png").convert_alpha(), pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_12.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_13.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_14.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave/demon_cleave_15.png")]
demon_at2 = [pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_1.png").convert_alpha(),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_2.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_3.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_4.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_5.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_6.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_7.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_8.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_9.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_10.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_11.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_12.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_13.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_14.png"),pygame.image.load("Game Assets/Mobs/Demon King/demon_cleave_left/demon_cleave_15.png")]

#Status demonio
vida_demon = 150
dano_tomado = 0
demon_attacking = False
demon_atacou = False
demon_cronometro = 0
demon_direction = -1