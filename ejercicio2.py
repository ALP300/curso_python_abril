'''

Validación de acceso: 
Solicita usuario, contraseña y rol (admin, editor, visitante). 
Verifica si las credenciales 
son válidas y muestra los permisos disponibles según el rol. 
Usa múltiples condicionales 
y lógica anidada. 

'''
usuario_correcto="Admin"
contraseña_correcta="admin123"

usuario= input("Ingresa tu usuario: ")
contraseña= input("Ingresa tu contraseña: ")
rol= input("Ingresa tu rol (administrador,editor,visitante): ")

if usuario==usuario_correcto and contraseña==contraseña_correcta:
    if rol=="administrador":
        print("Acceso concedido al administrador")
        print("Permisos: Vista completa, edicion y eliminacion")
    elif rol=="editor":
        print("Acceso concedido al editor")
        print("Permisos: solo edicion")
    elif rol=="visitante":
        print("Acceso concedido al visitante")
        print("Permisos: solo lectura")
    else:
        print("Rol no valido")
else:
    print("Credenciales incorrectas")
