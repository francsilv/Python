tamanho = input("Digite o tamanho do arquivo para download: ")
tamanho = float(tamanho)
velocidade = input("Digite a velocidade do link: ")
velocidade = float(velocidade)
tempo_segundos = tamanho / velocidade
tempo_minutos = tempo_segundos / 60
tempo_minutos = round(tempo_minutos,2)
print(tempo_minutos)