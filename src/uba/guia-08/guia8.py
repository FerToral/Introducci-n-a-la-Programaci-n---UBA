from random import randint
from random import shuffle

import math
from queue import LifoQueue as Pila
from queue import Queue as Cola


def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila:
    p = Pila()
    for _ in range(cantidad):
        p.put(randint(desde, hasta))
    
    return p

def cantidad_elementos(p: Pila) -> int:
    count: int = 0
    back_pila = Pila()
    
    while not p.empty():
        back_pila.put(p.get()) 
        count+=1
    
    while not back_pila.empty():
        p.put(back_pila.get())
        
    return count


           
def buscar_el_maximo(p:Pila) -> int:
    back_pila = Pila()
    max: int = p.get()
    
    back_pila.put(max)

    while not p.empty():
        num:int = p.get()
        back_pila.put(num)    
        if num > max:
            max = num
    
    while not back_pila.empty():
        p.put(back_pila.get())
    
    return max

def print_pila(p:Pila):
    back_pila = Pila()
    elem: int
    while not p.empty():
        elem = p.get()
        back_pila.put(elem)   
        print(elem) 
    while not back_pila.empty():
        p.put(back_pila.get())

def buscar_nota_maxima(p: Pila) -> tuple[str,int]:
    back_pila = Pila()
    max_nota: tuple[str,int] = p.get()
    back_pila.put(max_nota) 

    while not p.empty():
        nota: tuple[str,int] = p.get()
        back_pila.put(nota) 
        if nota[1] > max_nota[1]:
            max_nota = nota
    
    while not back_pila.empty():
        p.put(back_pila.get())
    
    return max_nota

def esta_bien_balanceada(s:str) -> bool:
    
    balance = Pila()

    for c in s:
        if c == '(':
            balance.put('(')
        elif c == ')':
            if balance.empty():
                return False
            balance.get()
        
    return balance.empty()
 
def es_opeador(c:str) -> bool:
    return c == '+' or c == '-' or c == '*' or c == '/'

def operacion(c: str, a:int, b:int) -> float:
    res: float
    match c:
        case '+': res = a+b
        case '-': res =a-b
        case '*': res = a*b
        case '/': res = a/b
    return res


def evaluar_expresion(s:str) -> float:
    
    res = Pila()
    a: int
    b: int

 
    for c in s.split():
        if not es_opeador(c):
            res.put(int(c))
        else:
            b = res.get()
            a = res.get()
            res.put(operacion(c,a,b))
    
    return res.get()
             

def intercalar(p1: Pila, p2: Pila) -> Pila:

    back_p1 = Pila()
    back_p2 = Pila()
    res_inv = Pila()
    res = Pila()

    while not p1.empty():
        a = p1.get()
        b = p2.get()

        res_inv.put(b)
        res_inv.put(a)

        back_p1.put(a)
        back_p2.put(b)
    
    while not back_p1.empty():
        p1.put(back_p1.get())

    while not back_p2.empty():
        p2.put(back_p2.get())
    
    while not res_inv.empty():
        res.put(res_inv.get())

    return res



        
        

    




def generar_nros_al_azarv2(cantidad:int, desde:int, hasta:int) -> Cola:
    c = Cola()
    for _ in range(cantidad):
        c.put(randint(desde, hasta))
    
    return p
    
def tam(c: Cola) -> int:
    cont: int = 0
    back_c = Cola()
    while not c.empty():
        back_c.put(c.get())
        cont+=1
    
    while not back_c.empty():
        c.put(back_c.get())
    
    return cont

def buscar_el_maximov2(c: Cola) -> int:
    max: int = c.get()
    c.put(max)

    for _ in range(tam(c)-1):
        elem: int = c.get()
        if elem > max:
            max = elem
        c.put(elem)
    
    return max

def buscar_nota_minima(c:Cola[tuple[str,int]]) -> tuple[str, int]:
    min: int = c.get()
    for _ in range(tam(c)-1):
        elem: int = c.get()
        if elem[1] < min[1]:
            min = elem
        c.put(elem)
    
    return min
    

def intercalar(c1: Cola, c2: Cola) -> Cola:
    res = Cola()   
    for _ in range(tam(c1)):
        elemA = c1.get()
        elemB = c2.get()
        res.put(elemA)
        res.put(elemB)
        
        c1.put(elemA)
        c2.put(elemB)
    
    return res


def armar_secuencia_bingo() -> Cola[int]:
    
    list_n: list[int] = list(range(100))
    shuffle(list_n)    

    bolillero = Cola()
    for bolilla in range(list_n):
        bolillero.put(bolilla)

    return bolillero

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    
    cont: int = 0

    for _ in range(tam(bolillero)):
        num: int = bolillero.get()
        for i in range(len(carton)):
            if num == carton[i]:
                cont+=1
        bolillero.put(num)

    return  cont

def pacientes_urgentes(c: Cola[tuple[int, str, str]]) -> int:

    cont: int = 0

    for _ in range(tam(c)):
        paciente: tuple[int, str, str] = c.get()
        if paciente[0] < 4:
            cont+=1
        c.put(paciente)
    
    return  cont



def atencion_a_clientes(c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str,int,bool,bool]]:
    clientes_prioridad = Cola()
    clientes_preferencial = Cola()
    clientes_restantes = Cola()
    for _ in range(tam(c)):
        paciente = c.get()
        if paciente[3]:
            clientes_prioridad.put(paciente)
        elif paciente[2]:
            clientes_preferencial.put(paciente)
        else:
            clientes_restantes.put(paciente)
        
        c.put(paciente)
    
    for cola in (clientes_preferencial, clientes_restantes):
        while not cola.empty():
            clientes_prioridad.put(cola.get())

    return clientes_prioridad
    


def print_cola(c:Cola):
    back_cola= Cola()
    elem: int
    while not p.empty():
        elem = p.get()
        back_cola.put(elem)   
        print(elem) 
    while not back_cola.empty():
        p.put(back_cola.get())


p: Pila = generar_nros_al_azar(5,6,9)
#print(print_pila(p))

print(print_pila(p))
print("El max:", buscar_el_maximo(p))
print(print_pila(p))

#Diccionarios

def pertenece(s: list[T], e: T) -> bool:

    for x in s:
        if x == e:
            return True
    
    return False


def promedio(notas: list[str,float], estudiante: str) -> float:
    cont: int = 0
    suma: int = 0
    for nota in range(notas):
        if nota[0] == estudiante:
            cont+=1
            suma+= nota[1]
    
    return suma/cont

def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str, float]:
    dic_notas: dict[str, float] = dict()
    estudiantes: list[str] = []
    
    for nota in range(notas):
        if not pertenece(dic_notas.keys(), nota[0]):
            dic_notas[nota[0]] = promedio(notas, nota[0])
        
    return dic_notas


def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str):

    if usuario in historiales:
        historiales[usuario].put(sitio)
    else:
        pila_nueva = Pila()
        pila_nueva.put(sitio)
        historiales[usuario] = pila_nueva




def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    sitio_actual = historiales[usuario].get()
    return sitio_actual


def agregar_producto( inventario: dict[str, dict[str, int | float]], nombre: str, precio: float, cantidad: int):
    inventario[nombre] = {
        'precio': precio,
        'cantidad': cantidad
    }

def actualizar_stock(inventario: dict[str, dict[str, int | float]], nombre: str, cantidad: int):
    inventario[nombre]['cantidad'] = cantidad
    # detalle_producto = inventario[nombre]
    # detalle_producto['cantidad'] = cantidad

def actualizar_precio(inventario: dict[str, dict[str, int | float]], nombre: str, precio: float):
    inventario[nombre]['precio'] = precio

def calcular_valor_inventario(inventario: dict[str, dict[str, int | float]]) -> float:
    res: float = 0
    # for key in inventario.keys():
    #     res+= inventario[key]['precio'] * inventario[key]['cantidad']
    for key, data in inventario.items():
        res+= data['precio'] * data['cantidad']
    return res
