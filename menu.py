from variaveis_menu import *
import select_dificuldade
from variaveis import *

from demon import *

def men():
    delay = 1
    while(True):
        janela_menu.set_background_color([0,0,0])
        fundo_menu.draw()
        
        jogar.draw()
        if mouse_menu.is_over_object(jogar):
            jogar_select.draw()
            if (mouse_menu.is_button_pressed(1)and delay >=0.5):
                delay = 0
                return True

        dificuldade.draw()
        
        if (mouse_menu.is_over_object(dificuldade) and delay>=0.5):
            dificuldade_select.draw()
            if mouse_menu.is_button_pressed(1):
                select_dificuldade.dificuldade()
                delay = 0
        

        sair.draw()

        if (mouse_menu.is_over_object(sair) and delay>=0.5):
            sair_select.draw()    
            if mouse_menu.is_button_pressed(1):
                return False        
        
        if delay<=1:
            delay = delay + 1*janela_menu.delta_time()
        janela_menu.update()
