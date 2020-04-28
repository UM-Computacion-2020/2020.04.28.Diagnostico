class CompuTools:

    def is_sorted(self,lista):
        ordenado=False
        self.a=lista
        for i in range(len(self.a)-1):
            if self.a[i]<self.a[i+1]:
                ordenado = True
            else:
                ordenado = False
                break
        return ordenado
