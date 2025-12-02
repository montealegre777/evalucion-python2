usuarios={
    10901:{"nombre":"catalina forero",
            "contraseña":"Qwe1rt#a",
            "saldo":"10000",
            "movimientos":[]
           
           },
    11123:{"nombre":" Miguel Triana",
            "contraseña":"A123bx$n",
            "saldo":"20000",
            "movimientos":[]
           
           }
    }
print("bienvenido al sistema ")
print("tiene 3 intentos para ingresar sus datos")

intentos=3
documento=0
while intentos>0:
        doc=int(input("ingrese docuento"))
        
        if doc in usuarios:
            documento=doc
            print("bienvenido",usuarios[doc]["nombre"])
            break
        else:
            intentos=intentos-1
            print("documento no encontrado",intentos)
if documento==0:
    print("acceso denegado, saliendo...")
    quit()
    
intentos=3
while intentos>0:
    contraseña=(input("igrese contraseña"))
    if contraseña==usuarios[documento]["contraseña"]:
        print("acceso exitoso")
        break
    else:
        intentos=intentos-1
        print("contraseña incorrecta")
if intentos==0:
    print("acceso denegado")
    quit()
          
saldo=10000 
opc=""
while opc != "5":
    print("menu de opciones: ")
    print("1. ver saldo")
    print("2. consignar")
    print("3. retirar")
    print("4. ver moviminetos")
    print("5. salir")
    opc=(input("selecciones una opcion"))
    
    match opc:
        case "1":
            print("su saldo actual es ",saldo)
        case "2":
            monto= int(input("ingrese monto (minimo 5000)"))
            if monto >=5000:
                saldo=saldo+monto
                
                print("consignacion exitosa, su saldo nuevo es ",saldo)
            else :
                print("el monto minimo es (5000)")
        case "3":
                monto=int(input("ingrese monto (minimo 5000)"))
                if monto >= 5000:
                    if monto<=saldo:
                        saldo=saldo-monto
                        print("retiro exitoso")
                    else:
                        print("saldo insuficiente")
                else:
                        print ("el monto minimo es 5000")
        case"4":
                if usuarios[documento]["movimientos"]==[]:
                    print("no hay movimientos")
                else:
                    for mov in usuarios[documento]["movimientos"]:
                        print("_",mov)
        case "5" :
            print("hatsa luego",usuarios[documento]["nombre"])
        case _:
            print("opcion invalida")
            
                    
                
            
        
            
            
            
            
            
            
            
            
            
            
    