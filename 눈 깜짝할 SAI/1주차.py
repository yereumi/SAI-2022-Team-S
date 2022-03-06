## 2

```
def rec(a):
    if a == 0:
        return 1
    return a * rec(a - 1)


print(rec(3))

rec3 = lambda a: a == 0 and 1 or a * rec(a - 1)
print(rec3(3))
```

## 3

# 신예지
import random
marble = random.randrange(1, 100)
print(marble)
count = 0

while True :
  num = int(input())
  count += 1
  if count == 6 :
    print("우리 깐부사이는 아니잖아~ 탕탕")
    break
  if num == marble :
    print("네가.. 뭐라고 했더라..?")
    break
  elif num < marble :
    print("UP")
  else :
    print("DOWN")

# 최서영

import random
marble=random.randrange(1,00)
trial=6

print(marble)

while trial>0:
  user=int(input())
  if user>marble:
    print("DOWN")
  elif user<marble:
    print("UP")
  else:
    print("'네가..뭐라고 했더라..?'")
    break #eexit(0)
  trial=trial-1
  if trial==0:
    print("'우리 깐부사이는 아니잖아~탕탕'")

# 박성열 뒤에서 첫째..!
import random
marble = random.randrange(1, 100)

for i in range(6):
    num=int(input());

    if i == 5 and marble != num:
        print("우리 깐부사이는 아니잖아~ 탕탕")
    elif num < marble:
        print("UP")
    elif num > marble:
        print("DOWN")
    else:
        print("네가.. 뭐라고 했더라..?")
        break

# 이수영
import random

marble = random.randrange(1,100)
i = 0
print(f"정답:{marble}")
while i < 6:
    a = int(input())
    if (a < marble):
        if (i == 5):
            print("우리 깐부사이는 아니잖아~ 탕탕")
            break
        print("UP")
    elif (a > marble):
        if (i == 5):
            print("우리 깐부사이는 아니잖아~ 탕탕")
            break
        print("DOWN")
    else:
        print("네가..뭐라고 했더라..?")
        break
    i+=4

## 4

# 신예지
n1, n2, n3, n4 = input().split(" ")

mylist = ['+', '-', '*', '/', '%']

for i in mylist :
    for j in mylist :
        if i == j :
            continue
        elif eval(f"{n1}{i}{n2}{j}{n3}") == eval(n4) :
            print(f"{n1}{i}{n2}{j}{n3}={n4}")

# 박성열
op = ['+', '-', '*', '/', '%']
#operate
In = list(map(str, input().split()))
#input
for i in range(5):
    for j in range(5):
        if j==i: continue #중복 처리

        result = eval(In[0]+op[i]+In[1]+op[j]+In[2]) #연산 결과 저장

        if result == int(In[3]): 
            print("%s%s%s%s%s=%s" %(In[0], op[i], In[1], op[j], In[2], In[3]))

# 감사합니다 쩔어...>< 멋집니다.

# 이수영 4 짧으면 간지다!
a,b,c,d = input().split()
s = ['+', '-', '*', '/', '%']
for i in s: #오..!
    for j in s:
        if (j!=i):
            if (int(d)==eval(f'{a}{i}{b}{j}{c}')):
                print(f'{a}{i}{b}{j}{c}={d}')

## 5

# 박성열
m, k, k2, n = map(int, input().split())

ar1=[] #ar1 배열 선언
ar2=[] #ar2 배열 선언

for i in range(m): #배열 ar1 생성
    ar = list(map(int, input().split()))
    ar1.append(ar)

for i in range(k2): #배열 ar2 생성
    ar = list(map(int, input().split()))
    ar2.append(ar)

result=[]

for i in range(m): #행렬곱
    ar=[]

    for j in range(n):
        mul=0
        #num=0

        for h in range(k):
             #if num == k: #필요 없는 건가요.?!.?!
                #num = 0

            mul += ar1[i][h]*ar2[h][j]
            #num+=1

        ar.append(mul)
    result.append(ar)

print(result)

# 이수영 5번 #멋지다..!
m,k,k1,n = input().split()
mat1 = []
mat2 = []

for i in range(int(m)):
    mat1.append(list(map(int,input().split())))
for i in range(int(k)):
    mat2.append(list(map(int,input().split())))

ans_matrix = []

for i in range(int(m)):
    sub_matrix = []
    for j in range(int(n)):
        tmp = 0
        for K in range(int(k)):
            tmp += mat1[i][K] * mat2[K][j]
        sub_matrix.append(tmp)
    ans_matrix.append(sub_matrix)
print(ans_matrix)