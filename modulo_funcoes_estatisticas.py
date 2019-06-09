import math
import os

def entrada_dados():
    dados = []
    
    total_valores = int(input("\n>>> Informe a quantidade de valores: "))
    
    print()
    
    for i in range(total_valores):
        dados.append(int(input(">>> Informe o valor %d -> " %(i+1))))
        
    return dados
    
    
def freq_absoluta(dados):
    freq_a = {}
    
    for valor in dados:
        freq_a[valor] = dados.count(valor)
        
    print("\n>>> Frequência absoluta: %s" %freq_a)
    
    
def freq_relativa(dados):
    freq_r = {}
    
    for valor in dados:
        freq_r[valor] = ((dados.count(valor)/len(dados)) * 100)
        
    print("\n>>> Frequência relativa: %s" %freq_r)
    
    
def media_aritmetica(dados):
    media_a = sum(dados)/len(dados)
    
    print("\n>>> Média = %.2f" %media_a)
    
    
def moda(dados):
    l_moda = []

    repeticoes = 0
    
    for valor in dados:
        aparicoes = dados.count(valor)
        if aparicoes > repeticoes:
            repeticoes = aparicoes
            
    for valor in dados:
        aparicoes = dados.count(valor)
        if aparicoes == repeticoes and valor not in l_moda:
            l_moda.append(valor)
            
    print("\n>>> Moda = ", l_moda)
    
    
def mediana(dados):
    dados.sort()
    
    if len(dados) % 2 == 0:
        r_mediana = (dados[int(len(dados)/2) - 1] + dados[int(len(dados)/2)])/2
    else:
        r_mediana = dados[int(len(dados)/2)]
        
    print("\n>>> Mediana = ", r_mediana)
    
    
def amplitude(dados):
    r_amplitude = max(dados) - min(dados)
    
    print("\n>>> Amplitude = ", r_amplitude)
    
    
def variancia_populacional(dados):
    soma = 0
    
    for valor in dados:
        soma += pow(valor - (sum(dados)/len(dados)),2)
    variancia_p = soma / len(dados)
    
    print("\n>>> Variância populacional = ", variancia_p)
    
    
def variancia_amostral(dados):
    soma = 0
    
    for valor in dados:
        soma += pow(valor - (sum(dados)/len(dados)),2)
    variancia_a = soma / (len(dados) - 1)
    
    print("\n>>> Variância amostral = ", variancia_a)
    
    
def desvio_populacional(dados):
    soma = 0
    
    for valor in dados:
        soma += pow(valor - (sum(dados)/len(dados)),2)
    variancia_p = soma / len(dados)
    desvio_p = math.sqrt(variancia_p)
    
    print("\n>>> Desvio populacional = ", desvio_p)
    
    
def desvio_amostral(dados):
    soma = 0
    
    for valor in dados:
        soma += pow(valor - (sum(dados)/len(dados)),2)
    variancia_a = soma / (len(dados) - 1)
    desvio_a = math.sqrt(variancia_a)
    
    print("\n>>> Desvio amostral = ", desvio_a)
    
    
def exibir_dados(dados):
    print("\n>>> Dados: %s" %(dados))
    
    
def menu():
    print('-' * 40)
    print("          Estatística Básica")
    print('-' * 40)
    print()
    print("1. Entrada do conjunto de dados")
    print("2. Exibir conjunto de dados")
    print("3. Frequência absoluta")
    print("4. Frequência relativa")
    print("5. Média aritmética")
    print("6. Moda")
    print("7. Mediana")
    print("8. Amplitude")
    print("9. Variância populacional")
    print("10. Variância amostral")
    print("11. Desvio padrão populacional")
    print("12. Desvio padrão amostral")
    print("13. Limpar o terminal")
    print("0. Encerrar o programa\n")
    
    return (int(input("Escolha uma opção: ")))
    
    
dados = []
dados_ordenados = []

while True:
    escolha = menu()
    
    if escolha == 1:
        dados = entrada_dados()
        dados_ordenados = sorted(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 2:
        exibir_dados(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 3:
        freq_absoluta(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 4:
        freq_relativa(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 5:
        media_aritmetica(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 6:
        moda(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 7:
        mediana(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 8:
        amplitude(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 9:
        variancia_populacional(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 10:
        variancia_amostral(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 11:
        desvio_populacional(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 12:
        desvio_amostral(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
        
    elif escolha == 13:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
    elif escolha == 0:
        print("\n>>> Programa encerrado com sucesso!\n")
        break
        input("\n>>> Pressione <ENTER> para continuar...\n")