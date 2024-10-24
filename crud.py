# CRUD básico en Python

# Inicializar 'base de datos' en una lista
data = []

# Función para crear un nuevo registro
def create_item(item):
    data.append(item)
    print(f'Item "{item}" agregado con éxito.')

# Función para leer todos los registros
def read_items():
    if data:
        print("Items actuales en la base de datos:")
        for idx, item in enumerate(data, 1):
            print(f"{idx}. {item}")
    else:
        print("La base de datos está vacía.")

# Función para actualizar un registro
def update_item(index, new_item):
    if 0 <= index < len(data):
        data[index] = new_item
        print(f'Item en posición {index + 1} actualizado a "{new_item}".')
    else:
        print("Índice fuera de rango.")

# Función para borrar un registro
def delete_item(index):
    if 0 <= index < len(data):
        removed_item = data.pop(index)
        print(f'Item "{removed_item}" eliminado con éxito.')
    else:
        print("Índice fuera de rango.")

# Menú básico
def menu():
    while True:
        print("\n--- CRUD en Python ---")
        print("1. Crear Item")
        print("2. Leer Items")
        print("3. Actualizar Item")
        print("4. Eliminar Item")
        print("5. Salir")

        option = input("Selecciona una opción: ")

        if option == '1':
            item = input("Introduce el nuevo item: ")
            create_item(item)
        elif option == '2':
            read_items()
        elif option == '3':
            read_items()
            index = int(input("Selecciona el índice del item a actualizar: ")) - 1
            new_item = input("Introduce el nuevo valor: ")
            update_item(index, new_item)
        elif option == '4':
            read_items()
            index = int(input("Selecciona el índice del item a eliminar: ")) - 1
            delete_item(index)
        elif option == '5':
            break
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
