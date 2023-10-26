from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import jogar
import dificuldade
import sair

janela = Window(1080,720)
janela.set_title("Blood Moon Ascension")
janela.set_background_color([0,0,0])
tecla = Window.get_keyboard()
click = Window.get_mouse()

background = GameImage("fundo_vila.png")
ground = Sprite("ground.png")
botao_jogar = Sprite("z_jogar.png")
botao_dificuldade = Sprite("z_dificuldade.png")
botao_sair = Sprite("z_sair.png")

while True:
    janela.set_background_color([0,0,0])

    jogar.jogar(janela, tecla, click, botao_jogar,ground,background)
    dificuldade.dif(janela,tecla,click,botao_dificuldade)
    sair.sair(janela,click,botao_sair)

    janela.update()