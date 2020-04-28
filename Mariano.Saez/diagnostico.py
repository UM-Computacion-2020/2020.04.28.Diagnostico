class CompuTools:
    def is_sorted(self, lista):
        ordered = False
        for i in range(len(lista)-1):
            if lista[i] < lista[i+1]:
                ordered = True
            else:
                return False
        return ordered
