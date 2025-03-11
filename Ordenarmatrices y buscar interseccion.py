import random
n = 10

matriz_1 = [[random.randint(0, 1000) for j in range(n)] for i in range(n)]

vector_1 = [valor for sublista in matriz_1 for valor in sublista]
vector_ordenado1 = sorted(vector_1)
print("\nMatriz ordenada:")
for i in range(0, len(vector_ordenado1), n):
    print(vector_ordenado1[i:i+n])
    
matriz_2=[[random.randint(0, 1000) for j in range(n)] for i in range(n)] 

vector_2 = [valor for sublista in matriz_2 for valor in sublista]
vector_ordenado2 = sorted(vector_2)
print("\nMatriz ordenada num2:")
for i in range(0, len(vector_ordenado2), n):
    print(vector_ordenado2[i:i+n])   

valores_vector_ordenado2=set(vector_ordenado2)
valores_vector_ordenado1=set(vector_ordenado1)
valores_compartidos=valores_vector_ordenado2.intersection(vector_ordenado1)
print("valores que ambas matrices comparten",valores_compartidos)
