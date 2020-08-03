from datetime import date, time, datetime, timedelta 
# 'date' apenas para data - 'time' apenas para horario
# 'datetime para data e hora - 'timedelta' para calculos com datas  

def trabalhando_com_date():

    data_atual = date.today()  # data atual - formato americano YYYY-MM-DD 
    print(data_atual.strftime('%d/%m/%y')) # Muda o formato da data(pode ser '/' '-' qualquer divisao)-- ### obs: se 'y' minusculo mostra 2 digitos se 'Y' maiusculo mostra 4 digitos
    print(data_atual.strftime('%A %d %B %Y')) # todos maiusculos e converte em string  -- 'A' = dia da semana

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S')) #converte em string desta forma

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %h:%M:%S'))  # Formatando para padrao brasileiro
    print(data_atual.strftime('%c'))
    print(data_atual.year)   # pode trazer dados separados 

    # trazer as semanas traduzidas
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()]) # weekday traz em numero a semana -- ex: data_atual[2] 

    #calculo com datas

    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15, weeks=2)
    print(nova_data)




if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()