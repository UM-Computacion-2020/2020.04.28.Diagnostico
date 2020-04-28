class CompuTools:

    def is_sorted(self,lista):
        self.a=lista[0]
        self.b=lista[1]
        self.c=lista[2]
        self.d=lista[3]
        if self.d>self.c and self.c>self.b and self.b>self.a:
            return True
        else:
            return False
