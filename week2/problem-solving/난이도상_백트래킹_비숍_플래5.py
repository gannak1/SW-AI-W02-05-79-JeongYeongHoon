# 백트래킹 - 비숍 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1799

input_chess = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
]

# input_chess = []
# for i in range(int(input())):
#     input_chess.append(list(map(int, input().split())))

# 검은 칸 / 흰 칸을 어떻게 나눌까?

# 각 칸의 두 대각선 번호를 어떻게 표현할까?

# DFS에서 “놓는다 / 안 놓는다”를 어떻게 분기할까?
black_coordinate = [[0] * 5 for _ in range(5)]
white_coordinate = [[0] * 5 for _ in range(5)]


def main(input_chess):
    1


print(main(input_chess))
