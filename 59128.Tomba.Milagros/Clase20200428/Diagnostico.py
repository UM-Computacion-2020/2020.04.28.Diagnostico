class CompuTools():
    def is_sorted(self, compu):
        n = len(compu)
        m = 0
        for m in range(1, n):
            for j in range(n-1):
                if compu[j] > compu[j+1]:
                    return False
        return compu
        
        
    
    
      
