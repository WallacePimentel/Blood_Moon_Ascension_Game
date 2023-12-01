from variaveis_menu import *

def dificuldade():
    select_diff = False
    delay = 0

    while(not select_diff):

        janela_menu.set_background_color([0,0,0])
        fundo_menu.draw()
        
        facil.draw()
        if mouse_menu.is_over_object(facil):
            facil_select.draw()
            if mouse_menu.is_button_pressed(1):
                select_diff = True
                

        medio.draw()
        if (mouse_menu.is_over_object(medio) and delay >=0.5):
            medio_select.draw()
            if mouse_menu.is_button_pressed(1):
                select_diff = True
        
        dificil.draw()
        if mouse_menu.is_over_object(dificil):
            dificil_select.draw()
            if mouse_menu.is_button_pressed(1):
                select_diff = True
        
        janela_menu.update()
        if delay<=1:
            delay = delay + 1*janela_menu.delta_time()
        
        if teclado_menu.key_pressed("esc"):
            select_diff = True