#Bibliotecas Necessarias
import csv                        #Criar arquivo do excel
import json                       #ler os dados anotados em json
import pandas as pd               #Mostrar tabela no Terminal
import matplotlib.pyplot as plt   #Criar grafico de barra
import os                         #Criar/Testar arquivos e pastas

#carregou data
with open('data.json', 'rt') as arq:
    data = json.load(arq)

#Organizando Dados
labels = list(data.keys())
fa = list(data.values())
faTot = sum(fa)
faAcum = 0
fr = [item*100/faTot for item in fa]
frTot = sum(fr)
frAcum = 0
"""
labels = sorted(set(data))                    #Amostras
fa = [data.count(label) for label in labels]  #F.a.
faTot = sum(fa)                               #Soma das F.a.
faAcum = 0                                    #F.a. Acumulada
fr = [item*100/faTot for item in fa]          #F.r. 
frTot = sum(fr)                               #Soma das F.r.
frAcum = 0                                    #F.r. Acumulada
"""
#cabeçalho da tabela
csvData = [ ["Streaming", "F.a.", "F.a.(Acum)", "F.r.(%)", "F.r.(Acum)"] ]

#dados da tabela
for i in range(len(labels)):
    faAcum += fa[i]
    frAcum += fr[i]
    csvData.append([
        labels[i],                 #Streaming
        fa[i],                     #F.a.
        faAcum,                    #F.a. Acumulado
        "{:.0f}%".format(fr[i]),   #F.r.(%)
        "{:.0f}%".format(frAcum)   #F.r Acum
    ])


#rodapé
csvData.append(["Total", faTot, "-", f"{frTot:.0f}%" , "-"])

#cria pasta Result se não existir
if not(os.path.isdir('Result')):
    os.mkdir('Result')

#salva arquivo csv
with open('Result/TabelaDeFrequencia.csv', 'wt+') as arq:
    csv.writer(arq).writerows(csvData)

#saida de Textos no Terminal
print('Resultados: ')
print(f'Tabela de Frequência salva em: {os.getcwd()}/Result/TabelaDeFrequencia.csv')
print(f'Grafico de Barras salvo em: {os.getcwd()}/Result/GraficoDeBarras.png')
print()
print(pd.read_csv('Result/TabelaDeFrequencia.csv'))

#configs do Grafico de barras
plt.title('Streaming Preferido')
plt.xlabel('Streaming')
plt.ylabel('Frequência Absoluta')
plt.bar(labels, fa)
plt.yticks(range(max(fa) + 1))
plt.savefig('Result/GraficoDeBarras.png')
