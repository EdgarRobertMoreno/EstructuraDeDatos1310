Detalle = {
                "Mesa" : 3 ,

                "Comensales" : 2 ,
                
                "Platos" : {

                            "Entrada" : "Ensalada verde" ,

                            "Medio" : "Crema de Zanahoria" ,

                            "Fuerte" : "Filete" ,
                } ,

                    "Adicionales" : {

                        "Entrada" :  "Ensalada sin ninguna semilla" ,

                        "Medio" : "Adereso Ranch", 

                        "Fuerte"  : "Filete Termino Medio" 

                        }

}

print("Mesa:" , Detalle["Mesa"])
print("Comensales:", Detalle["Comensales"])
print("Entrada:" , Detalle["Platos"]["Entrada"])
print("Medio:" , Detalle["Platos"]["Medio"])
print("Fuerte:" , Detalle["Platos"]["Fuerte"])
print(Detalle["Adicionales"]["Entrada"] , "," , Detalle["Adicionales"]["Medio"], "," , Detalle["Adicionales"]["Fuerte"])