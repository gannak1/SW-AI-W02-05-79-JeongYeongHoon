# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978


# 몇번 시도해도 안된 이유
"""
sqrt로 소수 범위 정하는 부분에서 마지막 숫자가 포함이 안되서 문제가 발생 (5.1 -> 5 -> 4까지 소수 검사 실행)
-> +1을 하여 극복
"""
# unique_count에 얼마나 있는지 담을 예정
# 요소가 0보다 같거나 작으면 다음으로 (같거나 안넣어도 다음 로직에서 걸러 지므로 문제 X)
# 요소가 1과 같으면 다음으로
# 요소가 2면 unique_count에 1을 더하고 다음으로
# 요소가 2로 나눠지면 다음으로
# 모든 각 리스트의 숫자의 값을 제곱근 한 값까지
# (이유는 제곱근보다 크면 이미 곱한 숫자가 나오므로)
# 그리고 1부터 +2하면서 range 함수로 모두 % 연산자로 나눠서 0이 되는지 검사,
# 0이 되는 것이 하나라도 있으면 다음으로
# 모두 하고 난 뒤에 return으로 unique_count 리턴
import math

n = int(input())
m = list(map(int, input().split()))


unique_count = 0

for i in range(len(m)):
    if m[i] <= 0:
        continue
    elif m[i] == 1:
        continue
    elif m[i] == 2:
        unique_count += 1
        continue
    elif m[i] % 2 == 0:
        continue
    else:
        is_plus = True
        for j in range(3, int(math.sqrt(m[i])) + 1, 2):
            if m[i] % j == 0:
                is_plus = False
                break
        if is_plus:
            unique_count += 1

print(unique_count)
