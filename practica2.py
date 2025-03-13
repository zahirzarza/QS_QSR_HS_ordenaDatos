import time
import random
import sys
sys.setrecursionlimit(300000)


#QuickSort
def QuickSort(A,p,r):
    if p<r:
        q=Particionar(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)


def Particionar(A,p,r):
    
    x=A[r]
    i=p-1

    #Hasta r para tomar en cuanta el ultimo valor del arreglo 
    for j in range (p, r): 
        if A[j]<=x:
            i=i+1
            A[i], A[j] = A[j],A[i]
    
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

#QuickSort Random

def QuickSortRandom(A,p,r):
    if p<r:
        q=ParticionarRandom(A,p,r)
        QuickSortRandom(A,p,q-1)
        QuickSortRandom(A,q+1,r)


def ParticionarRandom(A,p,r):
    k = random.randint(p,r)
    x=A[k]
    i=p-1

    #Hasta r para tomar en cuanta el ultimo valor del arreglo 
    for j in range (p, r): 
        if A[j]<=x:
            i=i+1
            A[i], A[j] = A[j],A[i]
    
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def MaxHeapify(A,i,tmHeap): #i donde se encuantra el nodo padre , tmHeap tamaño del heap
    izq = 2*i+1 #hijo izquierdo
    der = 2*i+1 #hijo derecho

    posMax = i
    if izq < tmHeap and A[izq] > A[der]:
        posMax = izq

    if der < tmHeap and A[der] > A[posMax]:
        posMax = izq

    if posMax != i:
        A[i], A[posMax] = A[posMax], A[i]
        MaxHeapify(A, posMax, tmHeap)

def InitMAxHeap(A): #Consruir MaxHeap
    n = len(A)
    for i in range (n//2, -1, -1):
        MaxHeapify(A, i,n)


def HeapSort(A):
    InitMAxHeap(A)
    tmHeap = len(A)
    for i in range (len(A)-1, 0, -1): #len(A)-1 como es iclusivo, y se cuenta desde el cero| 0, por que es exclusivo y queremos llegar a una posicion antes
        A[0], A[i] = A[i], A[0]
        tmHeap -= 1
        MaxHeapify(A, 0, tmHeap)


def Pruebas(lista):
    #Declaracion de las variables de tiempo
    tPQS = 0
    tPQSR = 0
    tPHS = 0
    m = len(lista)

    for i in range(3):
        a = lista[:] #Se copia la lista oiginal
        tInicial = time.perf_counter()
        QuickSort(a,0,m-1)
        tFinal = time.perf_counter()
        tiempo = tFinal - tInicial
        tPQS = (tPQS + tiempo)

    tPQS = (tPQS/3)

    for i in range(3):
        b = lista[:] #Se copia la lista oiginal
        tInicial2 = time.perf_counter()
        QuickSortRandom(b,0,m-1)
        tFinal2 = time.perf_counter()
        tiempo2 = tFinal2 - tInicial2
        tPQSR = (tPQSR + tiempo2)

    tPQSR = (tPQSR/3)

    for i in range(3):
        c = lista[:] #Se copia la lista oiginal
        tInicial3 = time.perf_counter()
        HeapSort(c)
        tFinal3 = time.perf_counter()
        tiempo3 = tFinal3 - tInicial3
        tPHS = (tPHS + tiempo3)
    
    tPHS = (tPHS/3)

    
    return tPQS, tPQSR, tPHS #se retornan los tiempos promediados
  
#Requerimiento 2
LM = [3,6,5,7,8,9,6,2,4,1]
A=LM[:]
B=LM[:]
C=LM[:]

print("Requerimiento 2")
print("QuickSort---------------")
print("Lista origina: ", A)
tInicial = time.perf_counter()
QuickSort(A,0,(len(A)-1))
tFinal = time.perf_counter()
tiempo = tFinal - tInicial
print("Lista ordenada: ", A, " en t: ", tiempo)

print("QuickSortRandom-----------")
print("Lista origina: ", C)
tInicial2 = time.perf_counter()
QuickSort(C,0,(len(C)-1))
tFinal2 = time.perf_counter()
tiempo2 = tFinal2 - tInicial2
print("Lista ordenada: ", C, " en t: ", tiempo2)

print("HeapSort---------------")
print("Lista origina: ", B)
tInicial3 = time.perf_counter()
HeapSort(B)
tFinal3 = time.perf_counter()
tiempo3 = tFinal3 - tInicial3
print("Lista ordenada: ", B, " en t: ", tiempo3)

#Requerimiento 3
print("Requerimiento 3")

n =20000

lista1 = list(range(0,n)) #lista ascendente
lista2 = list(range(n,0,-1)) #Lista decendente
lista3 = [random.randint(-100,100) for _ in range(n)] #Lista aleatoria

#calculo de tiempo para el mejor caso
tPQS, tPQSR, tPHS = Pruebas(lista1) 
print("---------------------------------------------")
print(" Caso Mejor para n= ", n)

print("QuickSort")
print("Tiempo: ", tPQS)

print("Quick Sort Random")
print("Tiempo: ", tPQSR)

print("Heap Sort")
print("Tiempo: ", tPHS)


#calculo de tiempo para el peor caso
tPQS, tPQSR, tPHS = Pruebas(lista2)
print("---------------------------------------------")
print(" Caso Peor para n= ", n)

print("QuickSort")
print("Tiempo: ", tPQS)

print("Quick Sort Random")
print("Tiempo: ", tPQSR)

print("Heap Sort")
print("Tiempo: ", tPHS)

#calculo de tiempo para el caso promedio
tPQS, tPQSR, tPHS = Pruebas(lista3)
print("---------------------------------------------")
print(" Caso promedio para n= ", n)

print("QuickSort")
print("Tiempo: ", tPQS)

print("Quick Sort Random")
print("Tiempo: ", tPQSR)

print("Heap Sort")
print("Tiempo: ", tPHS)