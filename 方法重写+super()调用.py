class a:
    def eat(self):
        print('1')
    
class b:
    def chi(self):
        print(2)
class c(a,b):
    def eat(self):
        super().eat()
        print('hello')
    def chi(self):
        return super().chi()
    
C=c()
C.eat()
C.chi()
