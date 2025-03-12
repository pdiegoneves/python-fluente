class Teste():
    def __init__(self, valor, valor2=None):
        self.valor = valor
        self.valor2 = valor2


    def __bool__(self):
        return bool(self.valor2)

teste = Teste(1)

if teste:
    print('verdadeiro')
else:
    print('falso')


