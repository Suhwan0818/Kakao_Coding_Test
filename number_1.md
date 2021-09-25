# 1번 문제  
```py
from bisect import bisect_left # bisect 라이브러리 중 left값을 찾는 함수를 사용
```  
이진 탐색 구현을 도와주는 bisect 라이브러리를 사용한다.  
## bisect 라이브러리란?  
**bisect 라이브러리**는 **원소들이 정렬된 리스트에서 특정 원소를 찾을 때 효과적**이다. bisect 라이브러리는 아래 2가지 함수가 가장 중요한다.  
1. **bisect_left(list, data):** 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지)  
2. **bisect_right(list, data):** 리스트에 데이터를 삽입할 가장 오른쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지)  
   
예를 들어, 아래와 같은 ***그림 1*** 과 같이 a라는 리스트[1, 2, 3, 3, 5, 10]가 있을 때, 새로운 데이터 3을 삽입하려고 할 때의 bisect_left()와 bisect_right() 함수는 각각 **2** 와 **4** 를 반환한다.  
![bisect_function](/img/bisect_function.PNG)  
위의 예제를 파이썬으로 구현하면 다음과 같다  
```py
from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 5, 10]
x = 3

print("bisect_left: {bisect_left(a, x)}") # 2
print("bisect_right: {bisect_right(a, x)}") #4
```  
이와 같은 두 함수의 특성 덕분에 bisect_left()와 bisect_right()는 **원소들이 정렬된 리스트에서 특정 범위 내에 속하는 특정 값의 개수를 구할 대 효과적**이며 **O(logN)**으로 빠르게 계산 할 수 있다는 장점이 있다.  

```py
from bisect import bisect_left # bisect 라이브러리 중 left값을 찾는 함수를 사용
from itertools import combinations # iterable에서 원소 개수가 r개인 조합 뽑기
```  
## itertools  
**itertools: 효율적인 루핑을 위한 이터레이터를 만드는 함수**  
문제 해결을 위해 사용한 combinations는 **조합형 이터레이터**이다. 코드로 예시를 보겠다.  
```py
from itertools import combinations
row  = [1, 2, 3]
for column in combinations(row, 2):
    print(column) #(1, 2) (1, 3) (2, 3) ...
```
combinations(iterable, r) 라고 가정을 하고 설명을 하자면 iterable에서 원소 개수가 r개인 조합 뽑기라고 보면된다.  
파이썬 공식문서에 따르면 입력 iterable의 순서에 따라 사전식 순서로 방출된다. 입력 iterable이 정렬되어있으면, **조합 튜플이 정렬된 순서로 생성**된다.  

```py
from bisect import bisect_left # bisect 라이브러리 중 left값을 찾는 함수를 사용
from itertools import combinations # iterable에서 원소 개수가 r개인 조합 뽑기

def make_all_cases(temp): #주어진 정보들을 하나씩 탐색해서 테이블처럼 자료를 만든다
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k): #표를 만든다는 느낌으로 이용
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx] #값을 넣어주고
                else:
                    case += '-' #비어있다면 그냥 - 로 대체
            cases.append(case)
    return cases
```

**make_all_cases** 함수는 주어진 정보들을 하나씩 읽어내서 표와 같은 테이블 자료를 만들어내기 위한 함수이다.   
여기서 combinations의 역할은 표를 만들어 주는 역할을 할 것이다. 표를 만들며 들어갈 정보가 있다면 값을 넣어주고 비었다면 -를 채우는 식으로 이용했다.  
|||||
|:---:|:---:|:---:|:---:|
|조건1|조건2|조건3|조건4|조건5|
|-|조건6|조건7|조건8|-|
|-|-|조건9|-|조건10|
|조건11|-|-|-|-|  
위 예시와 같이 필요한 부분을 채우는 식으로 진행을 했다.  

```py
from bisect import bisect_left # bisect 라이브러리 중 left값을 찾는 함수를 사용
from itertools import combinations # iterable에서 원소 개수가 r개인 조합 뽑기

def make_all_cases(temp): #주어진 정보들을 하나씩 탐색해서 테이블처럼 자료를 만든다
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k): #표를 만든다는 느낌으로 이용
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx] #값을 넣어주고
                else:
                    case += '-' #비어있다면 그냥 - 로 대체
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.splite()) #위에서 만든 정보를 cases라는 변수에 다시 담아준다.
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else: all_people[case.append(int(seperate_info[4]))]
    
    for key in all_people.keys():
        all_people[key].sort() #정렬을 한번 해준다(시간 단축이 목표)

    for q in query: #query 정보들을 하나씩 탐색하고 모든 조건을 만족하고 기준 점수보다 높은 사람 수를 파악
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_p[4] + seperate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target]))) #아까 위에서 정렬을 해줘서 bisect_left가 상대적으로 빠르다.
        else:
    return answer
```