continuador = input('gostaria de usar a calcula maluca ? s ou n ?') 
while continuador == 's' or continuador == 'S' or continuador == 'sim' or continuador == 'Sim' or continuador == 'SIM' :      
    
    numero_1 = input('digite um numero ')
    numero_2 = input(' digite um segundo numero ')
    if numero_1.isnumeric() and numero_2.isnumeric():
      operador = input(' qual operador? ')
      numero_1 = float(numero_1)
      numero_2 = float(numero_2)
      if operador == '+':
        print(numero_1 + numero_2)  
      elif operador == '-':
        print(numero_1 - numero_2)
      elif operador =='x' or operador =='*' : 
        print(numero_1 * numero_2)
      elif operador =='/':
        print(numero_1 / numero_2)
      else:
        print('valor nao e um operador valido...')   
    else:
      print('um dos valores nao era bem um numero ne... to achando que voce e burro, so pode')
    continuador = input('gostaria de usar a calcula maluca ? s ou n ?') 
if  continuador =='n' or  continuador == 'N' or  continuador == 'nao' or continuador == 'Nao' or  continuador == 'NAO':
  print(' drogra... nao quer brincar com a calcula maluca ???? QUAL SEU PROBLEMA? VOCE E UM ANIMAL DE TETA!!! SOME DA KII. PORRA ') 
else:
  print('meu deus manoo... voce tem retardo ne! nao sabe o que é um s ou n... sim ou nao pqp meu irmao... para com essas mongoloidias ai que ja to sem paciencia... ')     