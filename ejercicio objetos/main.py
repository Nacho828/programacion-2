from Cliente import Cliente
from Empresa import Empresa


hector = Cliente(nombre="Hector", apellidos="Costa Guzman",
dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")
# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])
# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)
print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")
print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")
# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)