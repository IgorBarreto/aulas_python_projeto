from datetime import datetime

def salvar(nomeArquivoEntrada):
    arquivoEntrada =open(nomeArquivoEntrada,'r')
    nomeAluno =str(input('Qual é o seu nome? ')).strip()
    nomeAtividade = str(input('Qual é a atividade? ')).strip()
    if '.py' in nomeAtividade:
        nomeAtividade = nomeAtividade.replace('.py','')
    dataHoraAtual = datetime.now().strftime('%d%m%Y%H%M%S')
    nomeArquivoSaida =f'{nomeAluno}_' \
                      f'{nomeAtividade}_' \
                      f'{datetime.now().strftime("%d%m%Y%H%M%S")}.txt'

    arquivoSaida = open(nomeArquivoSaida,'w')

    for linha in arquivoEntrada:
        arquivoSaida.write(linha)
if __name__ == '__main__':
    arquivoEntrada = str(input('Qual o arquivo a ser salvo? '))
    salvar(arquivoEntrada)
    print('Arquivo salvo com sucesso')