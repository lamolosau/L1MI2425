from projetl1.triplets import add
from projetl1.triplets import mul
from projetl1.triplets import sub
from projetl1.triplets import dot
from projetl1.triplets import cross
from projetl1.triplets import times
from projetl1.triplets import length
from projetl1.triplets import hat

def test_add():
    t1 = (1,1,0)
    t2 = (2,3,4)
    t3 = add(t1,t2)
    assert t3 == (3,4,4)

def test_mul():
    t1 = (1,1,1)
    t2 = mul(t1,2)
    assert t2 == (2, 2, 2)

def test_sub():
    t1 = (1,1,1)
    t2 = (2,2,2)
    t3 = sub(t1,t2)
    assert t3 == (-1,-1,-1)

def test_dot():
    t1 = (1,1,1)
    t2 = (2,2,2)
    assert dot(t1,t2) == 6

def test_cross():
    t1 = (1,0,0)
    t2 = (0,1,0)
    t3 = cross(t1,t2)
    assert t3 == (0,0,1)

def test_times():
    t1 = (1,0.5,0.5)
    t2 = (0,0.5,0.5)
    t3 = times(t1,t2)
    assert t3 == (0,0.25,0.25)
    
def test_length():
    t1 = (1,2,2)
    assert length(t1) == 3
    
def test_hat():
    t1 = (1,2,2)
    t2 = mul(t1,1/3)
    assert hat(t1) == t2