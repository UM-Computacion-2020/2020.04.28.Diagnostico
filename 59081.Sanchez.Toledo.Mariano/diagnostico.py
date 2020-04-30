class CompuTools:
    def is_sorted (self, lista):
        n = len(lista)
        for i in range (n-1):
            if lista[i] < lista[i+1]:
                order = True
            else: 
                order = False
                break
        return order
