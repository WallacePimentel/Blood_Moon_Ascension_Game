from PPlay.window import *
from PPlay.sprite import *

janela_menu = Window(1080, 720)
janela_menu.set_title("Blood Moon ascesion")
janela_menu.set_background_color([0,0,0])

mouse_menu = Window.get_mouse()
teclado_menu = Window.get_keyboard()

#Fundos
fundo_inicial = Sprite("img/fundos/fundo_inicial.png")
fundo_menu = Sprite("img/fundos/menu.png")


#Botões
comecar = Sprite("img/botões/Começar.sem.selecionar.png")
comecar_select = Sprite("img/botões/Começar.selecionado.png")
comecar.set_position((janela_menu.width)*3/5, (janela_menu.height)*9/20)
comecar_select.set_position((janela_menu.width)*3/5, (janela_menu.height)*9/20)

jogar = Sprite("img/botões/jogar.sem.selecionar.png")
jogar_select = Sprite("img/botões/jogar.selecionado.png")
jogar.set_position(janela_menu.width/2 - jogar.width/2, janela_menu.height/2 - 40- 3*jogar.height/2)
jogar_select.set_position(janela_menu.width/2 - jogar.width/2, janela_menu.height/2 - 40 - 3*jogar.height/2)

dificuldade = Sprite("img/botões/dificuldade.sem.selecionar.png")
dificuldade_select = Sprite("img/botões/dificuldade.selecionada.png")
dificuldade.set_position(janela_menu.width/2 - dificuldade.width/2, janela_menu.height/2 - dificuldade.height/2)
dificuldade_select.set_position(janela_menu.width/2 - dificuldade.width/2, janela_menu.height/2 - dificuldade.height/2)

sair = Sprite("img/botões/sair.sem.selecionar.png")
sair_select = Sprite("img/botões/sair.selecionado.png")
sair.set_position(janela_menu.width/2 - sair.width/2, janela_menu.height/2 + 40 + sair.height/2)
sair_select.set_position(janela_menu.width/2 - sair.width/2, janela_menu.height/2 + 40 +sair.height/2)

facil = Sprite("img/botões/facil.sem.selecionar.png")
facil_select = Sprite("img/botões/facil.selecionado.png")
facil.set_position(janela_menu.width/2 - jogar.width/2, janela_menu.height/2 - 40- 3*jogar.height/2)
facil_select.set_position(janela_menu.width/2 - jogar.width/2, janela_menu.height/2 - 40 - 3*jogar.height/2)


medio = Sprite("img/botões/medio.sem.selecionar.png")
medio_select = Sprite("img/botões/medio.selecionado.png")
medio.set_position(janela_menu.width/2 - dificuldade.width/2, janela_menu.height/2 - dificuldade.height/2)
medio_select.set_position(janela_menu.width/2 - dificuldade.width/2, janela_menu.height/2 - dificuldade.height/2)

dificil = Sprite("img/botões/dificil.sem.selecionar.png")
dificil_select = Sprite("img/botões/dificil.selecionado.png")
dificil.set_position(janela_menu.width/2 - sair.width/2, janela_menu.height/2 + 40 + sair.height/2)
dificil_select.set_position(janela_menu.width/2 - sair.width/2, janela_menu.height/2 + 40 +sair.height/2)





