import os

productos = []


def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio y la cantidad.")
        return
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido correctamente.")


def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
        return
    print("\nLista de productos:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
    print()


def actualizar_producto():
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            try:
                producto["precio"] = float(input("Ingrese el nuevo precio: "))
                producto["cantidad"] = int(input("Ingrese la nueva cantidad: "))
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
            except ValueError:
                print("Error: Debe ingresar un número válido.")
                return
    print(f"No se encontró el producto con nombre '{nombre}'.")


def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    for i, producto in enumerate(productos):
        if producto["nombre"].lower() == nombre.lower():
            productos.pop(i)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"No se encontró el producto con nombre '{nombre}'.")


def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados en 'productos.txt'. Adiós!")


def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados desde 'productos.txt'.")


def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()
