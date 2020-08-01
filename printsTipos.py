# formas de printar Resultados concatenados
a = 10
b = 2

soma = a + b
subtracao = a - b
mult = a * b
divisao = a / b
resto = a % b
# print 1
print('Soma: ', soma, '\nSubitracao: ', subtracao, '\nMultiplicacao: ', mult, '\nDivisao: ', divisao, '\nResto: ', resto)

print('\n')
#print 2
print('Soma: {soma} \nSubtracao: {subtracao} \nMultiplicacao: {mult} \nDivisao: {divisao}'
'\nResto: {resto}'.format(soma=soma,
subtracao=subtracao, divisao=divisao, mult=mult, resto=resto))

print('\n')

#print 3
print('Soma: %s \nSubitracao: %s \nMultiplicacao: %s \nDivisao: %s \nResto: %s'% (soma, subtracao, mult, divisao, resto))


