# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

"재귀함수로 순열을 만들어서 array의 모든 조합을 구현한 후 해당하는 숫자를 넣어서 맞는지 틀린지 확인"

import copy

n = int(input())  # 인풋 부분
n_array = list(map(int, input().split()))  # 인풋 부분


def recursive(origin_array, max_number=-1):  # 재귀함수 부분0
    result = [
        max_number
    ]  # 결과, 최대값을 리스트로 받아서 지역함수 내에서도 글로벌처럼 사용하기 위해 선언
    current_array = []  # 현재 탐색

    def p_recursive(array):
        if len(current_array) == len(
            origin_array
        ):  # 만약 dfs로 탐색하여 추가한 array가 원본 배열과 동일하면 확인
            sum_factor = sum_function(
                current_array
            )  # 현재 dfs로 찾은 6자리 차이 합을 구하는 함수를 이용하여 값을 리턴
            if result[0] < sum_factor:  # 최대값보다 크면
                result[0] = sum_factor  # 최대값을 리턴
            return
        elif len(array) == 0:  # array의 길이가 0이면 다음으로
            return
        else:
            for i in range(len(array)):
                current_array.append(array[i])  # dfs에서 현재 위치를 추가
                p_recursive(array[:i] + array[i + 1 :])  # 다음 array로 순회
                current_array.pop()  # 끝나면 다음 행으로

    p_recursive(origin_array)
    return result


def sum_function(array):
    result = 0
    for i in range(len(array) - 1):
        result += abs(
            array[i] - array[i + 1]
        )  # 모든 값을 찾아서 절대값으로 차이를 모두 합하는 함수
    return result


print(recursive(n_array)[0])
