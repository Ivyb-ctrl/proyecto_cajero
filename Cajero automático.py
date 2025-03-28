base_datos =  {"Juan": 10000, "María": 20000, "Sofia": 100.000}
seleccion = 0
while seleccion >= 3:
    seleccion = int(input("¿Usted quién es?:\n0: Juan:\n1: María:\n2: Sofia\n3: SALIR\n"))
    
    # if seleccion == 0 or seleccion == 1 or seleccion == 2 or seleccion == 3:
    if seleccion in (0,1,2): 
        seleccion_cliente = list(base_datos.keys() ) [seleccion]
        print("El cliente seleccionado fue:", seleccion_cliente)
    
    if seleccion== 0:
        print("Usted es el cliente #1")
    elif seleccion== 1:
        print("Usted es el cliente #2")
        
    elif seleccion== 2:
        print("Usted es el cliente #3")
        
    elif seleccion== 3:
        print("Usted decidió SALIR")
    
    else: 
        print("Error: no seleccionó opción válida")

operacion = int(input("¿Usted qué acción desea realizar?:\n1: Consultar:\n2: Retirar:\n3: Consignar: \n4:SALIR"))

if operacion== 1:
    print("Este es el saldo de la cuenta:", base_datos)
elif seleccion== 2:
    print("Usted es el cliente #2")
    
elif seleccion== 3:
    print("Usted es el cliente #3")
    
elif seleccion== 4:
    print("Usted decidió SALIR")

else: 
    print("Error: no seleccionó opción válida")

