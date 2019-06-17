# RecursiveFunction
# 1. 기본 단계와 재귀 단계
> 숫자를 카운트 다운 하는 함수를 만들고 싶다고 하자. 그럼 어떻게 코딩할 것인가?  아래 라고 생각할 수 있지만, 멈추지 않는 코드라 문제가 된다. 이때 필요한 것이 기본 단계이다. 이렇게 재귀 에는 2개의 단계가 필요하다. 1) 기본 단계 2) 재귀 단계
```
def count_down(num):
	 print i 
	 return count_down(num-1)

```
> 아래 코드는 1) 기본 단계 2) 재귀 단계를 충족한 재귀함수이다.
```
def count_down(num)
	print i 
	if num <= 1: 
		return 
	else:
		count_down(num-1) 
```
> 정리하면...
1. 기본 단계 : 무한 반복을 막기 위해 꼭 필요하다.
2. 재귀 단계 : 자기 자신 함수 호출한다.

# 2. 문제 풀기 
## 2-1. 코드업(CodeUp) 재귀함수 문제 
* [2번. (재귀 함수) 1부터 n까지 역순으로 출력하기](https://github.com/JUNGEEYOU/RecursiveFunction/blob/master/1_2_codeup.py)
* [3번. (재귀 함수) 두 수 사이의 홀수 출력하기](https://github.com/JUNGEEYOU/RecursiveFunction/blob/master/1_3_codeup.py)  


