import pandas as pd
import matplotlib.pyplot as plt
# leitura dos dados CSV
dados = pd.read_csv('Versão APP.csv',sep=',')
dados['mes'] = pd.DatetimeIndex(dados['datatime'], yearfirst = True).month
dados['money'] = dados['money'].str.replace('$','')
dados['money'] = pd.to_numeric(dados['money'], errors='coerce')

def versao(u):#Função que permite o uso dos meses em formato numérico
    return pd.DataFrame(u.groupby('mes')['app version'].mean()).reset_index()

def media(m):# DEFINE A FUNÇÃO MÉDIA MENSAL
    return pd.DataFrame(m.groupby('mes')['money'].mean()).reset_index()


#imprime as opções de gráfico para o usuário escolher
print('Opção 1: Gráfico média mensal de valores')
print('Opção 2: Gráfico média por mes definido pelo usuário')
print('Opção 3: Finaliza o programa')

x = int(input('Qual opção gostaria de ver primeiro? '))  #da inicia o programa

while 1 <= x <= 3:


 
    if x == 1:
        mmensal = media(dados)  # INDICA A MÉDIA MENSAL DE VALORES
        # PLOTA O GRÁFICO DA MÉDIA DE VALORES PAGOS POR MÊS
        plt.title('Valores médios pagos por mês') 
        plt.grid()
        plt.plot(mmensal['mes'], mmensal['money'],marker = 'o', color = 'indigo') 
        plt.xticks(range(1,len(mmensal['mes']) + 1))
        plt.xlabel('mês') 
        plt.ylabel('media de valor pago') 
        plt.show() 
        x = int(input('digite 0 para iniciar: '))
    if x == 2:
        mes = int(input('Digite o mes escolhido: ')) # ESCOLHA DO MÊS FEITA PELO USUÁRIO
        # PARAMETROS PARA ESCOLHA DE MÊS
        while mes <= 0 :
            print('ERRO! MÊS INVALIDO')
            mes = int(input('Digite o mes escolhido: '))
        while mes >= 13:
            print('ERRO! MÊS INVALIDO')
            mes = int(input('Digite o mes escolhido: '))
        else:
            # PLOTA O GRÁFICO DOS VALORES PAGOS NO MÊS DE ESCOLHA DO USUÁRIO
            plt.title('Valores Pagos') 
            plt.plot(dados['money'][dados['mes'] == mes],marker = 'o', color = 'darkmagenta')
            plt.xlabel('usuarios') 
            plt.ylabel('preço pago')
            plt.show()
            x = int(input('digite 0 para iniciar: '))

    if x == 3: 
        #corpo do cogigo - histograma das versão do app                  
        print('digite o número correspondente ao mês desejado')
        print('exemplo: digite 1 pata janeiro, 2 para fevereiro e assim sucessivamente até 12 correspondente dezembro') 
        mes_versao = int(input('Qual mês gostaria de ver o histograma?  '))
        print()
        while True:
            if mes_versao>12 or mes_versao<=0:#if que checa a validade da informação dada pelo usuário 
                print('ERRO!!!! o número informado não corresponde a nenhum mês')        
                plt.title('número não corresponde a nenhum mês de nosso banco de dados')
                plt.xlabel('?????????????')
                plt.ylabel('?????????????')
                plt.show()
                mes_versao = int(input('Qual mês gostaria de ver o histograma?  ')) 
            else: 
                color = input('qual cor gostaria de ver os graficos? use as cores em inglês. ')
                plt.hist(dados['app version'][dados['mes'] == mes_versao],color=color)
                plt.title('Relação usuários/versão do app')
                plt.xlabel('Versão')
                plt.ylabel('usuários')
                plt.show()
                break



