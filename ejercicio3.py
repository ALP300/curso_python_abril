'''
Clasificación de productos: 
Pide nombre, precio y categoría (tecnología, alimentos, ropa). Dependiendo de la 
categoría y precio, aplica diferentes tipos de impuestos y clasificaciones 
(lujo, básico, 
etc.). 


'''
def clasificar_producto(nombre, precio, categoria):
    # Definimos reglas de impuestos según categoría y precio
    impuestos = 0
    clasificacion = "Básico"

    if categoria.lower() == "tecnología":
        if precio > 2000000:  # umbral de lujo
            clasificacion = "Lujo"
            impuestos = precio * 0.19 + precio * 0.04  # IVA + impuesto lujo
        else:
            impuestos = precio * 0.19  # IVA estándar

    elif categoria.lower() == "alimentos":
        if precio > 100000:  # alimentos caros considerados lujo
            clasificacion = "Lujo"
            impuestos = precio * 0.05  # impuesto reducido
        else:
            impuestos = 0  # exento

    elif categoria.lower() == "ropa":
        if precio > 300000:
            clasificacion = "Lujo"
            impuestos = precio * 0.19
        else:
            impuestos = precio * 0.10  # ropa básica con impuesto reducido

    else:
        clasificacion = "Desconocido"
        impuestos = 0

    return {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "clasificacion": clasificacion,
        "impuestos": impuestos,
        "precio_final": precio + impuestos
    }

print("=== Clasificación de productos ===")
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cat = input("Ingrese la categoría (tecnología, alimentos, ropa): ")
resultado = clasificar_producto(nombre, precio, cat)
print("\n--- Resultado ---")
print(f"Nombre: {resultado['nombre']}")
print(f"Precio: {resultado['precio']}")
print(f"Categoría: {resultado['categoria']}")
print(f"Clasificación: {resultado['clasificacion']}")
print(f"Impuestos: {resultado['impuestos']}")
print(f"Precio final: {resultado['precio_final']}")
   