import json
import csv

empresas = [
    {"rut": "72642413-6", "nombre": "Comercial Calcetas Runner", "ventas": 150000000},
    {"rut": "76437473-2", "nombre": "Reparación Mac           ", "ventas": 300000000},
    {"rut": "76254356-9", "nombre": "ProgramaSoftware         ", "ventas": 27500000},
    {"rut": "76077262-3", "nombre": "Calzados Roma            ", "ventas": 15000000},
    {"rut": "76310800-8", "nombre": "Empresa Arcos            ", "ventas": 80000000},
    {"rut": "76283690-4", "nombre": "Casino Coffe             ", "ventas": 120000000},
    {"rut": "76952985-5", "nombre": "Cafe Express ltda        ", "ventas": 50000000},
    {"rut": "76081440-2", "nombre": "Vino Export SA           ", "ventas": 20000000},
    {"rut": "76216579-1", "nombre": "Cepa Merl LTDA           ", "ventas": 30000000},
    {"rut": "76597875-0", "nombre": "Comercial Ropa America   ", "ventas": 60000000},
    {"rut": "76852106-3", "nombre": "Empresas JP              ", "ventas": 90000000},
    {"rut": "76887745-8", "nombre": "Empresas ICata SA        ", "ventas": 100000000},
    {"rut": "76210124-2", "nombre": "Buses Peñalolen          ", "ventas": 150000000},
    {"rut": "76802052-4", "nombre": "Sandias Paine LTDA       ", "ventas": 70000000},
    {"rut": "76575973-1", "nombre": "Modas Junior P           ", "ventas": 400000000},
    {"rut": "76869384-2", "nombre": "Bar del 81               ", "ventas": 250000000},
    {"rut": "76877803-6", "nombre": "Empresas LLS             ", "ventas": 8000000 }
]
def clasificar():
    for empresa in empresas:
        if empresa['ventas'] <= 100000000:
            empresa['clasificacion'] = "pequeño contribuyente"
        elif 100000001 <= empresa['ventas'] <= 200000000:
            empresa['clasificacion'] = "mediano contribuyente"
        elif empresa['ventas'] >= 200000001:
            empresa['clasificacion'] = "gran contribuyente"

    print("\nrut:\t\tnombre:\t\t\tventas:\t\tclasificacion")
    for empresa in empresas:
        
        if empresa["clasificacion"] == "pequeño contribuyente":
            print(f"{empresa["rut"]}\t{empresa["nombre"]} {empresa['ventas']}\t{empresa['clasificacion']}")

    print("\nrut:\t\tnombre:\t\t\tventas:\t\tclasificacion")
    for empresa in empresas:
        
        if empresa["clasificacion"] == "mediano contribuyente":
            print(f"{empresa["rut"]}\t{empresa["nombre"]} {empresa['ventas']}\t{empresa['clasificacion']}")

    print("\nrut:\t\tnombre:\t\t\tventas:\t\tclasificacion")
    for empresa in empresas:
        
        if empresa["clasificacion"] == "gran contribuyente":
            print(f"{empresa["rut"]}\t{empresa["nombre"]} {empresa['ventas']}\t{empresa['clasificacion']}")       

def guardar():
    with open("Empresas.json", "w") as file:
        json.dump(empresas, file,indent=4)
    print("\nArchivo Empresas.json creado correctamente ")    

def guardar_csv():
    with open("Empresas.csv","w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["rut","nombre","ventas", "clasificacion"])
        for empresa in empresas:
            writer.writerow([empresa["rut"],empresa["nombre"],empresa["ventas"],empresa["clasificacion"]])

    print("\nArchivo Empresas.csv creado correctamente ")        

def cargar():
    try:
        with open("Empresas.json", "r") as file:
            global empresas
            empresas=json.load(file) 
            print("\nArchivos cargados desde Empresas,json Exitoso")
            
            print("\nrut:\t\tnombre:\t\t\tventas:\t\tclasificacion")
            for empresa in empresas:
                print(f"{empresa["rut"]}\t{empresa["nombre"]} {empresa['ventas']}\t{empresa['clasificacion']}")

    except FileNotFoundError:
        print("Archivo Empresas,json no existe")  

def cargar_datos_csv():
    try:
        with open("Empresas.csv", 'r') as file:
            reader = csv.DictReader(file)
            global empresas
            empresas = [row for row in reader]
            print("\nDatos cargados desde Departamentos.csv")

            print("\nrut:\t\tnombre:\t\t\tventas:\t\tclasificacion")
            for empresa in empresas:
                print(f"{empresa["rut"]}\t{empresa['nombre']} {empresa['ventas']}\t{empresa['clasificacion']}")

    except FileNotFoundError:
        print("\nEl archivo Departamentos.csv no existe.")      

def menu():
    while True:
        print("\n\tDUOC EMPRESAS")
        print("1.Clasificar empresas")
        print("2.Guardar datos JSON")
        print("3.Guardar datos CSV")
        print("4.Cargar Datos JSON")
        print("5.Cargar Datos CSV")
        print("6.Salir")
        opc=input("\tOPC:")
        if opc=="1":
            clasificar()
        elif opc=="2":
            guardar()
        elif opc=="3":
            guardar_csv()
        elif opc=="4":
            cargar()
        elif opc=="5":
            cargar_datos_csv()
        elif opc=="6":
            print("Adios....")
            break
        else:
            print("Selecciones una opcion correcta...")

if __name__=="__main__":
    menu()