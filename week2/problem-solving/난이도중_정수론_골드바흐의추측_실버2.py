# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

"소수 찾는걸 응용해서 1부터"

import math

T = int(input())  # 몇개가 인풋될지 받을 인풋 부분

n = [int(input()) for i in range(T)]  # 직접 받을 숫자부분 인풋 부분

max_number = max(n)  # 최대 숫자
prime_list = []  # 소수 목록

# 처음부터 최대값까지 나눌 수 있는 소수를 미리 리스트에 넣어서 연산 최소화 i를 소수인지 아닌지 판별
for i in range(max_number + 1):
    if i == 2:
        prime_list.append(2)  # 2일 경우 소수
        continue
    elif i % 2 == 0:  # 2로 나눠질 경우 다음으로 진행
        continue
    is_prime = True  # 소수일 경우 리스트에 추가
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            is_prime = False  # 수소 중 하나라도 나눠지면 다음으로
            break
    if is_prime:
        prime_list.append(i)  # 소수 리스트 추가

for i in range(len(n)):
    for j in range(n[i] // 2, 1, -1):  # 나눌 수 있는 반까지 리스트를 쪼갬
        if j in prime_list:  # 소수 목록에 있으면 시작
            if (
                n[i] - j
            ) in prime_list:  # 원본 값에서 뺀 값이 소수 리스트에 있으면 리턴
                print(f"{j} {n[i] - j}")
                break
