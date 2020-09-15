import numpy as np

lista = [18,21,29,52,56]

vector=np.array(lista)

print(vector)
[18 21 29 52 56]

lista1 = [19,20,10,1]

vector2=np.array(lista1)

----> 1 print(vector+vector2)

ValueError: operands could not be broadcast together with shapes (5,) (4,) 
