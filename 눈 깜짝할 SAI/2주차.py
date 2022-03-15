## 1
4. Numpy를 사용하면 지난 주에 구현한 행렬곱을 함수 하나로 해결할 수 있다.

## 2
4. shape이 (2,2)인 행렬과 (1,3)인 행렬 사이에는 broadcasting이 발생하지 않는다.

## 3
# 차원을 고려하지 않고, 슬라이싱만 함.

from sklearn.datasets import load_iris
iris_raw = load_iris(as_frame=True)
iris_data = iris_raw['data']

iris_data = np.array(iris_data)

sl = iris_data[:, 0]
sw = iris_data[:, 1]
pl = iris_data[:, 2]
pw = iris_data[:, 3]

print(sl)
print(sw)
print(pl)
print(pw)

## 4
# 차원을 고려하지 않고, 슬라이싱만 함.

from sklearn.datasets import load_iris
iris_raw = load_iris(as_frame=True)
iris_data = iris_raw['data']

iris_data = np.array(iris_data)

sl = iris_data[:, 0]
sw = iris_data[:, 1]
pl = iris_data[:, 2]
pw = iris_data[:, 3]

print(sl)
print(sw)
print(pl)
print(pw)

## 5
import numpy as np
arr1=np.random.randint(1,51,(10,3))
arr2=np.random.randint(1,51,(10,3))

arr3=np.concatenate([arr1,arr2])
print(arr3)