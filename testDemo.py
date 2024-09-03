from multipledispatch import dispatch
class Polygon():
    
    @dispatch(int, int)
    def add(self,a,b):
        print(a+b)
        
    @dispatch(int, int, int)
    def add(self,a,b,c):
        print(a+b+c)
    
    @dispatch(float, float, float)
    def add(self,a,b,c):
        print(a+b+c)    
p = Polygon()
p.add(1,2)
p.add(3,4,5)
p.add(1.1,2.2,3.3)