#Criando uma aplicação que determina se o aluno foi aprovado ou não de acordo com a média
print('Bem vindo a aplicação\n')
a = int(input('Quantidade de provas: '))  # TOTAL DE AVALIAÇÕES DADA
soma = 0
print('------------------------------\n')
for i in range(a):
    nota = float(input('Digite a {}º nota: '.format(i+1)))  # DIGITAR A NOTA EM FORMATO DECIMAL
    soma = soma + nota
    

media = soma / a   
result = media * 10

if result > 100.0:  # No caso as notas serem de 0 a 100
    result = media
print('\n------------------------------')
print('Resultado final é: {}% \nSua media é: {}'.format(round(result, 2), media))
print('------------------------------')
if result >= 70.0:
    print('\nParabés voce está APROVADO')

if result >= 50.0 and result < 70.0:
    print('\nVoce esta de RECUPERAÇÃO')

if result < 50.0:
    print('\nVoce esta REPROVADO')


print("\n------------------------------\n-------Fim da aplicação------- \n------------------------------\n")
