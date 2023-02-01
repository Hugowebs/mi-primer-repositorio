def vehiculo (tipo, color):
    def __iinit__ (self,tipo,color):
        self.tipo= tipo
        self.color= color
        self.velocidad= 0

    def acelerar (self, velocidad):
        self.velocidad+= velocidad

         a1 = vehiculo
        a1.acelerar (30)
        a1.acelerar (20)
        a1.acelerar (10)



def factorial (numero):
        if (type(numero)!= int):
        return ("el numero debe ser entero")

    if(numero < 0):
        return ("El numero de ser positivo")

    if (numero > 1):
        numero = numero * factorial(numero - 1)
    
    return numero