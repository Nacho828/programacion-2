class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes


    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
            return
        print("Cliente no encontrado")


    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
            return
        print("Cliente no encontrado")