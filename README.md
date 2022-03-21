# Algorithm_python
> 자료구조와 알고리즘 유형정리 및 문제 풀이 😇  

## 1. Chapter 구성
*나동빈 저, 이것이 코딩 테스트다 with 파이썬*

|목차|유형|문제1|문제2|문제3|문제4|
|------|---|---|---|---|---|
|Chapter1|**그리디**|큰 수의 법칙|숫자 카드 게임|1이 될 때까지|
|Chapter2|**구현**|시각|왕실의 나이|게임 개발|
|Chapter3|**DFS,BFS**|음료수 얼려먹기 유형|미로탈출|
|Chapter4|**정렬**|위에서아래로|성적이낮은순서로학생출력하기|두배열의원소교체|
|Chapter5|**이진탐색**|부품찾기|떡볶이떡만들기|
|Chapter6|**다이나믹프로그래밍**|1로만들기|개미전사|바닥공사|효율적인화폐구성|
|Chapter7|**최단경로**|가장빠른길찾기|미래도시|전보|
|Chapter8|**그래프이론**|팀결성|도시분할계획|커리큘럼|

## 2. 유형정리

### (1) 그리디
최소한의 아이디어로 빠르게 또는 탐욕적으로 문제를 해결하는 방식.단순 문제 해결 방식.  
> 예시) 하나몬이 아르바이트를 하러 간 사이에, 안타깝게도 하나몬의 집에 도둑이 들었다.
도둑의 가방은 35kg까지의 물건만 담을 수 있고, 하나몬의 집에는 4개의 물건이 있다.

주로, 집계 함수나 경우의 수, 반복된 수열의 구조를 파악하여 문제를 해결한다.
> 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 그리디의 경우 -> 집계 함수, 경우의 수, 반복된 수열의 형태 중 어떤 접근 방식이 최적일 지 방법을 선택한다.
> 3. 코드의 전체적인 구조를 설계하고 접근법을 검토한다.  
     (최적의 해를 찾는 것이 아니므로, dynamic programming이랑 헷갈리지 말자.)

### (2) 구현
전체적인 구현 능력을 평가하는 유형.  
그리디에서는 문제 해결 과정을 보여준다면, 구현에서는 코드의 전체적인 구조를 **상세히** 설계하는 데에 초점.  

특별한 알고리즘 적용 없이, 문제의 요구사항에 맞게 코드를 작성하는 것이 핵심.  
++ 완전 탐색이나 시뮬레이션 유형에서 주로 요하는 문제.

> 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 완전 탐색의 경우 -> 주어진 데이터가 적을 때, 리스트 안의 요소를 검사하여 처리한다. 
> 3. 시뮬레이션의 경우 -> 상하좌우의 좌표 개념으로 접근.
> > - 상하좌우 각 좌표를 리스트화한 다음, 방문한 곳을 기록한다.  
> ex) steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]  
> > - 방문한 곳을 기록할 때, 리스트 컴프리헨션 방법을 이용한다.  
> ex)  d = [[0] * m for _ in range(n)]









