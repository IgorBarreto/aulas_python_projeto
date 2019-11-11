import pygame as pg
from random import randint

LARGURA = 600
ALTURA = 400
TAMANHO = 10
DEV = True
FPS=0
if DEV:
    FPS = 10
else:
    FPS = 30

# CORES
METADE_LARGURA = int(LARGURA / 2)
METADE_ALTURA = int(ALTURA / 2)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)


def desenhando_snake(tela, cor, px, py):
    pg.draw.rect(tela, cor, (px, py, TAMANHO, TAMANHO))


def gerar_posicao_maca():
    x = randint(0, LARGURA)
    y = randint(0, ALTURA)
    return x, y


def desenhando_maca(tela, cor, px, py):
    pg.draw.rect(tela, VERMELHO, (px, py, TAMANHO, TAMANHO))


def main():
    # INICIA O PYGAME
    pg.init()
    # CRIA UMA TELA COM O TAMANHO
    tela = pg.display.set_mode((LARGURA, ALTURA))
    # CRIA UM TÍTULO PARA A JANELA
    pg.display.set_caption('Snake')
    # VARIÁVEL PARA CONTROLAR O FPS
    relogio = pg.time.Clock()

    sair = False
    px_snake = METADE_LARGURA
    py_snake = METADE_ALTURA
    px_apple = randint(0, LARGURA - TAMANHO)
    py_apple = randint(0, ALTURA - TAMANHO)
    VELOCIDADE_X = 0
    VELOCIDADE_Y = 0
    while not sair:
        # FPS = 60
        relogio.tick(FPS)
        # PINTA A TELA DE BRANCO
        tela.fill(BRANCO)
        # FICA 'ESCUTANDO' QUAIS SÃO OS EVENTOS OCORRIDOS
        for evento in pg.event.get():
            # VERIFICA SE O EVENTO DE SAIR FOI CHAMADO
            if evento.type == pg.QUIT:
                # MUDA A VARIÁVEL SAIR PARA TRUE E SAI DO WHILE
                sair = True
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_F5 and DEV:
                    px_apple, py_apple = gerar_posicao_maca()
                if (evento.key == pg.K_LEFT) or (evento.key == pg.K_a):
                    VELOCIDADE_X = -10
                    VELOCIDADE_Y = 0
                if (evento.key == pg.K_RIGHT) or (evento.key == pg.K_d):
                    VELOCIDADE_X = 10
                    VELOCIDADE_Y = 0
                if (evento.key == pg.K_UP) or (evento.key == pg.K_w):
                    VELOCIDADE_Y = -10
                    VELOCIDADE_X = 0
                if (evento.key == pg.K_DOWN) or (evento.key == pg.K_s):
                    VELOCIDADE_X = 0
                    VELOCIDADE_Y = 10

        px_snake += VELOCIDADE_X
        py_snake += VELOCIDADE_Y
        desenhando_snake(tela, PRETO, px_snake, py_snake)
        desenhando_maca(tela, VERMELHO, px_apple, py_apple)
        pg.display.update()

        # ATUALIZA A TELA (QUADRO)

    # FECHA O PROGRAMA
    pg.quit()


if __name__ == '__main__':
    main()
