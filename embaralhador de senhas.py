import random
import string
import time

seg_baixa = string.ascii_letters + string.digits
seg_media = string.ascii_letters + string.punctuation
seg_alta = string.printable
senha_gerada = dados = ''


print('Escolha o nivel de segurança da senha'
                    '\n \033[32m[ 0 ] Levemente Segura\033[m '
                    '\n \033[33m[ 1 ] Segura\033[m '
                    '\n \033[31m[ 2 ] Muito Segura\033[m')
seguranca = int(input('Digite um valor baseado nos parametros: '))


while seguranca > 2 or seguranca < 0:
    print('\033[1:31mPARAMETROS INCORRETOS!\033[m')
    seguranca = int(input('Digite os valores baseados nos numeros apresentados!: '))
tamanho = int(input('Digite o comprimento da senha a ser gerado, serão aceitos somente valores entre 4 e 24: '))
while tamanho < 4 or tamanho > 24:
    print('\033[1:31mPARAMETROS INCORRETOS!\033[m')
    tamanho = int(input('Revise os parametros, os valores aceitos são somente entre \033[1:33m4 e 24\033[m: '))
    

if seguranca == 0:
    dados = '\033[32mSegurança Baixa\033[m'
    for i in range(tamanho):
        senha_gerada += str(random.choice(seg_baixa)).strip()
elif seguranca == 1:
    dados = '\033[33mSegurança Média\033[m'
    for i in range(tamanho):
        senha_gerada += str(random.choice(seg_media)).strip()
elif seguranca == 2:
    dados = '\033[31mSegurança Alta\033[m'
    for i in range(tamanho):
        senha_gerada += str(random.choice(seg_alta)).strip()
print('\033[1:35mProcessando dados com os parametros informados', end='')
time.sleep(0.7)
print(' .',end='')
time.sleep(0.7)
print(' .',end='')
time.sleep(0.7)
print(' .\033[m','\n')
time.sleep(0.5)

print('Sua senha com {} foi gerada: \033[7:48m{}\033[m'.format(dados,senha_gerada))

bancoSenhas = open('senhas.txt', 'a')
bancoSenhas.write('\n')
bancoSenhas.write(senha_gerada)

