#Codigo para importar y leer el json 
def open_json():
    import json
    with open("Pruebas.json", "r") as f:
        data = json.load(f)
    print(data)

def access():
    import json
    with open("Pruebas.json", "r") as f:
        data = json.load(f)
    #acceder a las mipymes dentro de la lista "mipymes"
    for mipymes in data["mipymes"]:
        #accedemos a los valores
        print(mipymes["name"])
        

def average():
    import json
    with open("Pruebas.json", "r") as f:
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

#devuelve una lista con los productos que hay en todas las mipymes, quitando los
def name_and_products():
    import json 
    with open ("Pruebas.json", "r") as f:
        data = json.load(f)
    list_prod=[]
    for mipymes in data["mipymes"]:
        #nombre de las mipymes y la cantidad de productos de las mypimes
        print(mipymes["name"])
        cant_pr = mipymes["products"]
        print(len(cant_pr))
        #lista que muestra los productos que hay en las mipymes, no hay productos repetidos  
        for prod in cant_pr:
            if prod not in list_prod:
                list_prod.append(prod["name"])
            else:
                print("no hay elementos")
    return list_prod

