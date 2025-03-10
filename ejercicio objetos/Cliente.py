class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
    
    
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)