class CompuTools():

    def is_sorted(self, lista):

        numerooriginal = []

        for i in lista:
            numerooriginal.append(i)

        n = len(lista)
        i = 0
        j = 0
        for i in range(1, n):
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        
       
        if(numerooriginal == lista):
            return True

        return False