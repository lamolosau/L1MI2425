import math


def add(t1: tuple[float,float,float],t2:tuple[float,float,float])-> tuple[float,float,float]:
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])

def sub(t1:tuple[float,float,float],t2:tuple[float,float,float])-> tuple[float,float,float]:
    return (t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2])

def mul(t:tuple[float,float,float],d:float)-> tuple[float,float,float]:
    return (t[0] * d, t[1] * d, t[2] * d)

def dot(t1:tuple[float,float,float],t2:tuple[float,float,float])-> float:
    return t1[0] * t2[0] + t1[1] * t2[1] + t1[2] * t2[2]

def cross(t1:tuple[float,float,float],t2:tuple[float,float,float]) -> tuple[float,float,float]:
    return (t1[1] * t2[2] - t1[2] * t2[1], t1[2] * t2[0] - t1[0] * t2[2], t1[0] * t2[1] - t1[1] * t2[0])

def times(t1:tuple[float,float,float],t2:tuple[float,float,float])-> tuple[float,float,float]:
    return (t1[0] * t2[0], t1[1] * t2[1], t1[2] * t2[2])

def length(t:tuple[float,float,float])-> float:
    return math.sqrt(t[0]**2 + t[1]**2 + t[2]**2)

def hat(t:tuple[float,float,float])-> tuple[float,float,float]:
    l = length(t)
    if l == 0:
        raise ValueError("t n'est pas un tuple normal")
    return (t[0] / l, t[1] / l, t[2] / l)
