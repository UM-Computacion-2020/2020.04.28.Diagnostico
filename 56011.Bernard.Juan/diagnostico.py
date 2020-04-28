class CompuTools():
    def is_sorted(self, compu):
        n = len(compu)
        i = 0
        for i in range(1, n):
            for j in range(n-1):
                if compu[j] > compu[j+1]:
                    return False
        return compu
