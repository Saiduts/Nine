import pandas as pd

Arc = "chicos.csv"
Ciu = {1: "Bucaramanga", 2: "Girón", 3: "Florida", 4: "Piedecuesta"}
Sex = {"M": "Masculino", "F": "Femenino"}

def cargar_datos():
    try:
        df = pd.read_csv(Arc, header=None, names=["codigo", "sexo", "nombre", "edad", "ciudad"])
        df_copy = df.copy()
        df_copy["ciudad"] = df_copy["ciudad"].map(Ciu)
        df_copy["sexo"] = df_copy["sexo"].map(Sex)
        print("\nDatos cargados exitosamente:\n")

        ##print(df_copy.to_string(index=False))
        ##print(df.to_string(index=False))
        
        return df, df_copy
    except Exception as e:
        print("Error", e)
        return pd.DataFrame()
    
def informe_especial(df, df_copy):
    if df.empty:
        print("No hay datos cargados")
        return
    print("\n--- Informe Especial ---\n")

    print(df_copy.to_string(index=False))

    ciu_tot=df["ciudad"].value_counts()
    tot_chicos = len(df)

    print("Distribucion por ciudad:")
    
    for ciudad, cantidad in ciu_tot.items():
        porc=(cantidad/tot_chicos)*100
        print(f"{ciudad}: {cantidad} niños ({porc:.2f}%)")
        
    print("\nDistribucion por edad:")
    grupos = {
        "Grupo 1 (0-5 años)": df[df["edad"] <= 5].shape[0],
        "Grupo 2 (6-10 años)": df[(df["edad"] > 5) & (df["edad"] <= 10)].shape[0],
        "Grupo 3 (+10 años)": df[df["edad"] >10].shape[0],
    }
    for grupo, cantidad in grupos.items():
        print(f"{grupo}: {cantidad} niños")

def operaciones(df):
    while True:
        print("*       Operaciones        *")
        print("* 1. Agregar niños.        *")
        print("* 2. Editar niño.          *")
        print("* 3. Eliminar niño.        *")
        print("* 4. Salir.                *")
        print("****************************")

        opcion= input("Seleccione una opción: ").lower()

        if opcion=="1":
            agregar_niño(df)
        elif opcion=="2":
            editar_niño(df)
        elif opcion=="3":
            eliminar_niño(df)
        elif opcion=="4":
            break
        else:
            print("Opcion invalida")

def agregar_niño(df):
    try:
        codigo = int(input("Ingrese código: "))
        sexo = input("Ingrese sexo (M/F): ").upper()
        nombre = input("Ingrese nombre: ").upper()
        edad = int(input("Ingrese la edad: "))
        ciudad = int(input("Ingrese la ciudad \n1. Bucaramanga \n2. Giron \n3. Florida \n4. Piedecuesta \nSeleccione la ciudad: "))
        
        
        if sexo not in Sex:
            print("Sexo invalido")
            return
        elif ciudad not in Ciu:
            print("Ciudad invalida")
            return

        df.loc[len(df)]=[codigo, sexo, nombre, edad, ciudad]
        print("Registro exitoso")
    except Exception as e:
        print("Error al agregar:", e)

def editar_niño(df):
    try:
        codigo = int(input("Ingrese el código del niño a editar: "))
        if codigo not in df["codigo"].values:
            print("Codigo invalido")
            return

        nuevonom = input("Ingrese el nuevo nombre: ").upper()
        nuevaedad = int(input("Ingrese la nueva edad: "))
        nuevaciudad = int(input("Ingrese la ciudad \n1. Bucaramanga \n2. Giron \n3. Florida \n4. Piedecuesta  \nSeleccione la ciudad: "))
        
        if nuevaciudad not in Ciu:
            print("Ciudad invalida")
            return

        df.loc[df["codigo"]==codigo, ["nombre","edad","ciudad"]]=[nuevonom, nuevaedad, nuevaciudad]
        print("Registro exitoso")
    except Exception as e:
        print("Error al editar:", e)

def eliminar_niño(df):
    try:
        codigo = int(input("Ingrese el código del niño a eliminar: "))
        if codigo not in df["codigo"].values:
            print("Codigo invalido")
            return

        df.drop(df[df["codigo"]==codigo].index, inplace=True) 
        print("Eliminacion exitosa")
    except Exception as e:
        print("Error al eliminar:", e)



def guardar_datos(df):
    try:
        df.to_csv(Arc, index=False, header=False)
        print("Guardado")
    except Exception as e:
        print("Error al guardar:", e)




def menu():
    df = pd.DataFrame()
    df_copy=df.copy()
    while True:
        print("\n********************************")
        print("*       Menú Principal        *")
        print("*----- Santiago Meneses ------*")
        print("********************************")
        print("* a. Cargar Datos.            *")
        print("* b. Informe Especial.        *")
        print("* c. Operaciones.             *")
        print("* d. Salir.                   *")
        print("********************************")

        opcion= input("Seleccione una opción: ").lower()

        if opcion=="a":
            df,df_copy=cargar_datos()
        elif opcion=="b":
            informe_especial(df, df_copy)
        elif opcion=="c":
            operaciones(df)
        elif opcion=="d":
            guardar_datos(df)
            break
        else:
            print("Opcion invalida")

if __name__ =="__main__":
    menu()



