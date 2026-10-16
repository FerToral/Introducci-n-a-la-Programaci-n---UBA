import math

def pertenece(s: list[int], e: int) -> bool:

    for x in s:
        if x == e:
            return True
    
    return False


def divide_a_todos(s: list[int], e: int) -> bool:
    
    for x in s:
        if x % e != 0:
            return False
        return True

def suma_total(s:list[int]) -> int:
    suma:int = 0
    for x in s:
        suma += x
    
    return suma

def maximo(s:list[int]) -> int:
    mayor:int = s[0]
    for x in s:
        if x >= mayor:
            mayor = x
    return mayor

def minimo(s:list[int]) -> int:
    minimo:int = s[0]
    for x in s:
        if x <= minimo:
            minimo = x
    return minimo

def ordenados(s:list[int]) -> bool:
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

def pos_maximo(s:list[int]) -> int:
    if len(s) == 0:
        return -1
    pos_max: int = 0
    for i in range(len(s)):
        if s[i] > s[pos_max]:
            pos_max = i
    return pos_max


def pos_minimo(s:list[int]) -> int:
    if len(s) == 0:
        return -1
    pos_max: int = 0
    for i in range(len(s)):
        if s[i] <= s[pos_max]:
            pos_max = i
    return pos_max
    
def long_mayorAsiete(s:list[str]) -> bool:
    for palabra in s:
        if len(palabra) > 7:
            return True
    return False

def es_palindroma(s:str):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1 -i]:
            return False
    return True

def iguales_consecutivos(s:list[int]) -> bool:
    if len(s) < 3:
        return False
    return True
   

my_list: list[int] = [1,2,3,4,5]
msg: str = "h"

res: bool = es_palindroma(msg)
#res: bool = ordenados(my_list)

print(res)