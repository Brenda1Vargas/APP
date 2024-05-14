# Diccionarios para almacenar información de usuarios, comercios y menús
clientes = {}
domiciliarios = {}
comercios = {
    "comercio1": {"menú1": ["plato1_comercio1", "plato2_comercio1"], "menú2": ["plato3_comercio1", "plato4_comercio1"]},
    "comercio2": {"menú1": ["plato1_comercio2", "plato2_comercio2"], "menú2": ["plato3_comercio2", "plato4_comercio2"]},
    "comercio3": {"menú1": ["plato1_comercio3", "plato2_comercio3"], "menú2": ["plato3_comercio3", "plato4_comercio3"]}
}

def solicitar_pedido(email):
    print("Bienvenido a la sección de pedidos.")
    print("Estos son los comercios disponibles:")
    for comercio in comercios:
        print(comercio)

    comercio_elegido = input("Por favor, elija un comercio: ")
    if comercio_elegido in comercios:
        print(f"Estos son los menús disponibles para {comercio_elegido}:")
        for menu in comercios[comercio_elegido]:
            print(menu)

        menu_elegido = input("Por favor, elija un menú: ")
        if menu_elegido in comercios[comercio_elegido]:
            print(f"Ha elegido el menú {menu_elegido} del comercio {comercio_elegido}.")

            # Selección del medio de pago
            medio_pago = input("¿Desea pagar con tarjeta o efectivo? ").lower()
            if medio_pago == "tarjeta":
                numero_tarjeta = input("Ingrese el número de su tarjeta: ")
                codigo_seguridad = input("Ingrese el código de seguridad de tres números: ")
                print("Pedido realizado. Su pedido será entregado pronto.")
            elif medio_pago == "efectivo":
                print("Pedido realizado. Por favor, tenga el dinero preparado para la entrega.")
            else:
                print("Opción de pago no válida.")
        else:
            print("Menú no válido.")
    else:
        print("Comercio no válido.")

def registrar_usuario(tipo_usuario):
    email = input("Ingrese su email: ")
    # Validar que el email contenga "@" antes de continuar
    if "@" not in email:
        print("Email no válido. Debe contener '@'.")
        return

    contraseña = input("Ingrese su contraseña: ")

    if tipo_usuario.lower() == "cliente":
        if email in clientes:
            print("Este email ya está registrado como cliente.")
        else:
            clientes[email] = contraseña
            print("Cliente registrado exitosamente.")
    elif tipo_usuario.lower() == "domiciliario":
        if email in domiciliarios:
            print("Este email ya está registrado como domiciliario.")
        else:
            domiciliarios[email] = contraseña
            print("Domiciliario registrado exitosamente.")

def login_usuario(tipo_usuario):
    while True:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")

        if tipo_usuario.lower() == "cliente" and clientes.get(email) == contraseña:
            print("Login de cliente exitoso.")
            solicitar_pedido(email)
            break
        elif tipo_usuario.lower() == "domiciliario" and domiciliarios.get(email) == contraseña:
            print("Login de domiciliario exitoso.")
            break
        else:
            print("Email o contraseña incorrectos. Inténtelo nuevamente.")

# Ejemplo de uso
print("Bienvenido a la app de domicilios!")
tipo_usuario = input("¿Desea registrarse como 'cliente' o 'domiciliario'? ").lower()  # Convertir a minúsculas
if tipo_usuario in ["cliente", "domiciliario"]:
    registrar_usuario(tipo_usuario)
    login_usuario(tipo_usuario)
else:
    print("Tipo de usuario no válido. Elija 'cliente' o 'domiciliario'.")
