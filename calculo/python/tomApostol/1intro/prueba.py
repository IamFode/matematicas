import axiomas

class Prueba(axiomas.Axioma):
    def prueba(self,x,y):
        return sum(x,y)

    
if __name__ == "__main__":
    p = Prueba()
    print(p.prueba(1,2))
