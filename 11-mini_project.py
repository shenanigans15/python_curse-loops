inventory = {
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galleta": 12,
}

cart = []
option = ""
ready = ""
total = 0

menu = """
¡Bienvenido a la tienda de dulces, DevCandy! 

      1. Agregar al carrito
      2. Eliminar del carrito
      3. Limpiar el carrito
      4. Pagar
      5. Salir

Dulces disponibles:
"""
inv = "\n".join(
    [f"   {candy.capitalize()} - ${price}" for candy, price in inventory.items()]
)

while option != "5":
    print(menu)
    print(inv)
    print()
    option = input("Elija una opción (1-4): ")
    if option == "1":
        while ready != "no":
            print()
            print(inv)
            print()
            add_cart = input("Agregue un dulce al carrito (): ").lower()
            if add_cart in inventory:
                cart.append(add_cart)
                print(f"{add_cart.capitalize()} agregado al carrito.")
            else:
                print()
            while True:
                ready = input(
                    "¿Desea agregar más golosinas al carrito? (si/no): "
                ).lower()
                if ready != "si" and ready != "no":
                    print("Escriba si o no.")
                else:
                    break
    elif option == "2":
        product = input("Ingresa el nombre del producto: ")
        if product in cart:
            cart.remove(product)
            print(f"{product.capitalize()} eliminado")
        else:
            print(f"No hay {product} en tu carrito")
    elif option == "3":
        if cart != []:
            cart.clear()
            print("Su carrito fue vaciado.")
        else:
            print("Su carrito está vacío.")
    elif option == "4":
        print("""
                   ____________
              >---| Tu carrito |---<
                   ¯¯¯¯¯¯¯¯¯¯¯¯ 
              """)
        for candy in cart:
            print(f"{candy.capitalize()} - ${inventory[candy]}")
            total += inventory[candy]
        print(f"Total a pagar: ${total}")
        print("Gracias por su compra.")
print("Hasta luego.")
