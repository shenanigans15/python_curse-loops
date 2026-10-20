# Crearás un carrito de compras que haga las siguientes funciones:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

menu = """

      ***********************************
      | Carrito de compras              |
      | Opciones:                       |
      | 1. Agregar producto             |
      | 2. Eliminar producto            |
      | 3. Mostrar la lista ordenada    |
      | 4. Buscar producto              |
      | 5. Contar productos del carrito |
      | 6. Vaciar el carrito            |
      | 7. Salir                        |
      ***********************************
      
      """
shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = ""

while option != "7":
    print(menu)
    option = input("Elige una opcion (1-7): ")
    if option == "1":
        product = input("Ingresa el nombre del producto: ")
        if product not in shopping_cart:
            shopping_cart.append(product)
            print("Producto agregado")
        else:
            print("El producto ya se encuentra en tu carrito")
    elif option == "2":
        product = input("Ingresa el nombre del producto: ")
        if product in shopping_cart:
            shopping_cart.remove(product)
            print("Producto eliminado")
        else:
            print("El producto no se encuentra en tu carrito")
    elif option == "3":
        if len(shopping_cart) > 0:
            shopping_cart.sort()
            print(shopping_cart)
        else:
            print("La lista está vacía")
    elif option == "4":
        product = input("Nombre del producto que desea buscar: ")
        if product in shopping_cart:
            print(f"{product} está en la lista")
        else:
            print("Producto no encontrado")
    elif option == "5":
        products_count = len(shopping_cart)
        print(f"Hay {products_count} productos en el carrito")
    elif option == "6":
        shopping_cart.clear()
        print("Lista vacía")
    else:
        print("Opción no válida")
else:
    print("Hasta luego")
