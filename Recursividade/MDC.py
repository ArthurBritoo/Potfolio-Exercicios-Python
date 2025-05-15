#14)  O máximo divisor comum (MDC) de dois números inteiros x e y pode ser calculado usando-se uma definição recursiva, como abaixo. Implemente este algoritmo.
#MDC(x, y) = MDC(x − y, y), se x > y
#MDC(x,y) = MDC(y,x)
#MDC(x,x) = x

def MDC(x,y):
    if x == y:
        return x
    if x > y:
        return MDC( x -y,y)
    else:
        return MDC(x, y - x)
