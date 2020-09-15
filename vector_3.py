import numpy as np

lista1 = [1,2,3,4]

lista2 = [1,2,3,4,5]

vector1 = np.array(lista1)

vector2 = np.array(lista2)

print(vector1+vector2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-28-5919b50d1cb4> in <module>
----> 1 print(vector1+vector2)

ValueError: operands could not be broadcast together with shapes (4,) (5,) 
