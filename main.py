from variaveis_menu import *
import menu

inic_jogo = False
while(True):
    janela_menu.set_background_color([0,0,0])
    
    fundo_inicial.draw()
    comecar.draw()
    if mouse_menu.is_over_object(comecar):
        comecar_select.draw()
        if mouse_menu.is_button_pressed(1):
            inic_jogo = menu.men()
    if teclado_menu.key_pressed("esc"):
        break
    if(inic_jogo):
        break
    janela_menu.update()

if(inic_jogo):
    import jogo
