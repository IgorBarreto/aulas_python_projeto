import pygame as pg
LARGURA =600
ALTURA = 400
METADE_LARGURA = int(LARGURA/2)
METADE_ALTURA = int(ALTURA/2)
PRETO =(0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)

def main():
    #INICIA O PYGAME
    pg.init()
    # CRIA UMA TELA COM O TAMANHO
    tela = pg.display.set_mode((LARGURA, ALTURA))
    # CRIA UM TÍTULO PARA A JANELA
    pg.display.set_caption('Snake')
    #VARIÁVEL PARA CONTROLAR O FPS
    relogio = pg.time.Clock()
    sair = False
    while not sair:
        #FPS = 60
        relogio.tick(60)
        #PINTA A TELA DE BRANCO
        tela.fill(BRANCO)
        #FICA 'ESCUTANDO' QUAIS SÃO OS EVENTOS OCORRIDOS
        for evento in pg.event.get():
            # VERIFICA SE O EVENTO DE SAIR FOI CHAMADO
            if evento.type == pg.QUIT:
                #MUDA A VARIÁVEL SAIR PARA TRUE E SAI DO WHILE
                sair=True
        #ATUALIZA A TELA (QUADRO)
        pg.display.update()
    #FECHA O PROGRAMA
    pg.quit()


if __name__ == '__main__':
    main()
