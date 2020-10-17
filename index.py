# importando dependências de terceiros

from prettytable import PrettyTable


# importando dependencias nativas 
from time import time
from random import sample

# importando algoritimos de ordenação
from seleção import seleção
from mergesort import mergesort
from quicksort import quicksort
from sort_interno import sort_interno

funções = [ mergesort,quicksort, seleção, sort_interno]

def calculoDeTempo(matriz_desordenada, tamanho_da_matriz):
	for função in funções:
		inicio = time()
		matriz_ordenada = função(matriz_desordenada)
		fim = time()
		total = fim - inicio
		tempoFormatado = round(total, 4)
		dicionario[tamanho_da_matriz].append(tempoFormatado)
        




   
dicionario = {
    "2000": [],
    "4000": [],
    "6000": [],
    "8000": [],
    "10000": [],
	"12000": [],
	"14000": [],
	"16000": [],
	"18000": [],
	"20000": [],
	"22000": [],
	"24000": [],
	"26000": [],
	"28000": [],
	"30000": [],
	"32000": [],
	"34000": [],
	"36000": [],
	"38000": [],
	"40000": [],
	"42000": [],
	"44000": []
}

table = PrettyTable([
    "n", "Mergesort", "Quicksort", "Selection", "Native"
    ])


print("Aluno: Valdir Evaristo da Silva Junior")
print("Aluno: Renato Gallo Borges Junior")
print("FATEC - Sao Jose dos Campos")
print("               time(s)")

inicio = time()
tempoFormatado = 0
i = "2000"
while(tempoFormatado <= 30):
	matriz = sample(range(int(i)), int(i))
	calculoDeTempo(list(matriz),i )
	row = [i] + dicionario[i]
	table.add_row(row)
	fim = time()
	total = fim - inicio
	tempoFormatado = round(total, 4)
	i = int(i)+ 2000
	i = str(i)
	
	
print(table)