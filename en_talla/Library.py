import json
#Codigo para importar y leer el json 
def open_json():
    import json
    
    with open("Pruebas.json", "r",encoding='utf-8') as f:
        data = json.load(f)
    return data

#abre directamente donde estan las mipymes 
def open_mipymes():
    import json
    
    with open("Pruebas.json", "r",encoding='utf-8') as f:
        data = json.load(f)
    dats = data["mipymes"]
    for i in range(len(dats)):
        print(dats[i])

def access():
    import json
    with open("Pruebas.json", "r",encoding='utf-8') as f:
        data = json.load(f)
    #acceder a las mipymes dentro de la lista "mipymes"
    for mipymes in data["mipymes"]:
        #accedemos a los valores, nombres de las mipymes en este caso
        print(mipymes["name"])
        

def average():
    import json
    with open("Pruebas.json", "r",encoding='utf-8') as f:
        data = json.load(f)
    list_pr_s=[]

    for mipymes in data["mipymes"]:
        products = mipymes["products"]
        #acceder a los precios dentro de la lista "products" y lo agrega a la lista creada
        for pro in products:
            pr_s = pro["price"]
            list_pr_s.append(pr_s)
    promedio = sum(list_pr_s)/len(list_pr_s)
    return promedio



#NO RECUERDO PARA QUE HICE ESTA

#devuelve una lista con los productos que hay en todas las mipymes, quitando los repetidos
def name_and_products():
    import json 
    with open ("Pruebas.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    dats_my = data["mipymes"]
    list_prod=[]
    for mipymes in dats_my:
        #nombre de las mipymes y la cantidad de productos de las mypimes
        cant_pr = mipymes['products']
        nombre = mipymes["name"]
    #lista que muestra los productos que hay en las mipymes, no hay productos repetidos  
        for prod in cant_pr:
            if prod not in list_prod:# lo que se va a agregar a la lista son el origen del producto
                list_prod.append(prod["category"])
            else:
                print("no hay elementos")
    return list_prod, nombre


