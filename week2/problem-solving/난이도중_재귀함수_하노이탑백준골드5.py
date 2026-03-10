# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

"""
하노이 n번째의 옮기는 상황을 가정하면
n-1개의 위에 있는 것들을 1번에서 2번으로 옮기고
n을 1번에서 3번으로 옮긴 다음
n-1개의 위에 있는 것들을 2에서 3으로 옮기면 완료
또한 첫번째 것은 1번에서 3번으로 옮기는게 첫번째다

이 과정을 재귀함수로 나타낸 것이다.
"""


top_height = int(input())  # 하노이 탑 수 인풋


def hanoi_number(
    n,
):  # 간단하게 하노이 계산하는 함수, 하나에 묶기에 로직이 복잡하여 20개 초과일 경우 대비하여 제작
    if n == 1:
        return 1
    else:
        return 2 * hanoi_number(n - 1) + 1


def hanoi(n, source, target, auxiliary):
    if n > 20:
        return  # 20개 초과일 경우 리턴하여 종료

    if n == 1:
        print(f"{source} {target}")  # 1일 경우 소스에서 타겟으로 옮기는 과정
    else:
        hanoi(
            n - 1, source, auxiliary, target
        )  # n번째 하노이 element를 옮기기 위해서 n-1까지의 과정을 보조 하노이 기둥으로 옮겨야함
        print(f"{source} {target}")
        hanoi(
            n - 1, auxiliary, target, source
        )  # n번째 하노이를 옮긴 후 보조 하누이 기둥에서 목표 하노이 기둥으로 옮김


hanoi_number(top_height)
hanoi(top_height, 1, 3, 2)
