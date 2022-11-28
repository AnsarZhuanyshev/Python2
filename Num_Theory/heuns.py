h = 0.5
x0 = -2 
xl = 0 
y0 = 0 

def f(x,y):
    return 7-x*y

def Eulers(x0,y0,xl,h):
    x = x0 
    while x < xl:
        x+=h 
        p = y0+h*f(x0,y0)
        y = y0 + h/2 * (f(x0,y0)+f(x,p))
        print(f'x={x},y={y}')
        x0 = x 
        y0 = y 

Eulers(x0,y0,xl,h)