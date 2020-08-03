class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    
    def power(self):
        if self.ligada:
            self.ligada = False

        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:      # verifica se esta ligada
            self.canal += 1  # aumenta 1 canal

    
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1  # diminui 1 canal




televisao = Televisao()
print('Televisao está ligada: {}'.format(televisao.ligada))

televisao.power()
print('Televisao está ligada: {}'.format(televisao.ligada))

televisao.power()
print('Televisao está ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
print('Televisao está ligada: {}'.format(televisao.ligada))
televisao.aumenta_canal()
televisao.aumenta_canal()

print('Canal: {}'.format(televisao.canal))

televisao.diminui_canal() 
print('Canal: {}'.format(televisao.canal))