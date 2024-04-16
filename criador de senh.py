import random
import string

def gerador_de_senha(frase):
    # Define o tamanho da parte nova da senha
    tamanho_novo = 10
    
    # Gera a parte nova da senha
    parte_nova = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho_novo))
    
    # Combina a frase fornecida com a parte nova
    senha = frase + parte_nova
    
    return senha

# Solicita uma frase do usuário
frase_usuario = input("Digite uma frase para gerar a senha: ")

# Gera a senha a partir da frase fornecida
senha_gerada = gerador_de_senha(frase_usuario)

# Exibe a senha gerada
print("A senha gerada é:", senha_gerada)
