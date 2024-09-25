# -*- coding: utf-8 -*-
import sys

# Inventario inicial de las diferentes categorías
inventario = {
    "herramientas": {
        "llavero allen": 10,
        "pinzas de corte": 15,
        "pinzas de punta": 12,
        "pinzas mecánicas": 8,
        "segueta": 5,
        "aspiradora": 3,
        "lava alfombra karcher": 2,
        "brocha 4": 20,
        "brocha 3": 25,
        "brocha 2": 30,
        "sopladora": 4,
        "cinta métrica": 10
    },
    "consumibles": {
        "kola loka": 50,
        "plastiacero": 40,
        "tinner": 30,
        "clarificador": 25,
        "cloro": 100,
        "alguisida": 60,
        "herbicida": 70,
        "mangueras": 15,
        "taza tanque": 10,
        "alimentador lavamanos": 10
    },
    "fijos": {
        "microondas": 2,
        "impresora": 5,
        "computadora": 10,
        "rack": 4,
        "estante": 3,
        "gabeta": 10,
        "mesa": 7,
        "escritorio": 6,
        "sillas": 12
    },
    "equipo mayor": {
        "caldera": 1,
        "secadora": 3,
        "lavadora": 5,
        "unidad paquete": 2
    }
}

# Función para mostrar el inventario actual
def mostrar_inventario():
    for categoria, items in inventario.items():
        print(f"\nCategoría: {categoria}")
        for item, cantidad in items.items():
            print(f"{item}: {cantidad}")

# Función para dar de alta o entrada de items al inventario
def dar_alta(categoria, item, cantidad):
    if categoria in inventario:
        if item in inventario[categoria]:
            inventario[categoria][item] += cantidad
            print(f"\n{cantidad} unidades de {item} añadidas a {categoria}.")
        else:
            inventario[categoria][item] = cantidad
            print(f"\n{item} añadido a {categoria} con {cantidad} unidades.")
    else:
        print(f"Categoría {categoria} no encontrada.")

# Función para dar salida de items del inventario
def dar_salida(categoria, item, cantidad):
    if categoria in inventario:
        if item in inventario[categoria]:
            if inventario[categoria][item] >= cantidad:
                inventario[categoria][item] -= cantidad
                print(f"\n{cantidad} unidades de {item} retiradas de {categoria}.")
            else:
                print(f"No hay suficientes unidades de {item}.")
        else:
            print(f"Item {item} no encontrado en {categoria}.")
    else:
        print(f"Categoría {categoria} no encontrada.")

# Menú principal
def menu():
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Mostrar inventario")
        print("2. Dar de alta entrada de items")
        print("3. Dar de baja o salida de items")
        print("4. Salir")
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            categoria = input("\nEscribe la categoría (herramientas, consumibles, fijos, equipo mayor): ").lower()
            item = input("Escribe el nombre del item: ").lower()
            cantidad = int(input("Escribe la cantidad a ingresar: "))
            dar_alta(categoria, item, cantidad)
        elif opcion == "3":
            categoria = input("\nEscribe la categoría (herramientas, consumibles, fijos, equipo mayor): ").lower()
            item = input("Escribe el nombre del item: ").lower()
            cantidad = int(input("Escribe la cantidad a retirar: "))
            dar_salida(categoria, item, cantidad)
        elif opcion == "4":
            print("Saliendo del sistema de inventario.")
            sys.exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Inicia el sistema de inventario
if __name__ == "__main__":
    menu()
