class CompuTools():

    def is_sorted(self, listaTest):
        n = len(listaTest) # Cuenta la cantidad de numeros de la lista
        for j in range(n-1): 
            if listaTest[j] < listaTest[j+1]: # Compara si un elemento de la lista es menor a su posterior 
                resultado = True
            else:
                resultado = False
                break # Debe realizar un break ya que si detecta un resultado falso no es necesario continuar
        return resultado
