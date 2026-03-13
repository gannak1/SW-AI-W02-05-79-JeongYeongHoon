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


def main(origin_input_chess):
    bishop_number = [0, 0]
    diag1 = [-1] * len(origin_input_chess) * 2
    diag2 = [-1] * len(origin_input_chess) * 2

    # 흑 인풋 생성]
    black_coordinate = []
    white_coordinate = []

    for i in range(len(origin_input_chess)):
        for j in range(len(origin_input_chess)):
            if origin_input_chess[i][j] == 0:
                continue
            elif origin_input_chess[i][j] != 0 and (i + j) % 2 == 0:
                black_coordinate.append([i, j])
            elif origin_input_chess[i][j] != 0 and (i + j) % 2 != 0:
                white_coordinate.append([i, j])

    # location = [[-1] * len(input_chess) for _ in range(len(input_chess))]
    def backtracking(input_chess, bishop_count, idx, index_number):
        coor_plus = input_chess[idx][0] + input_chess[idx][1]
        coor_minus = input_chess[idx][0] - input_chess[idx][1] + len(origin_input_chess)
        if diag1[coor_plus] != 1 and diag2[coor_minus] != 1:
            diag1[coor_plus] = 1
            diag2[coor_minus] = 1
            bishop_count += 1

            backtracking(input_chess, bishop_count, idx + 1, index_number)
            diag1[coor_plus] = -1
            diag2[coor_minus] = -1
            bishop_count -= 1
        if idx >= len(input_chess):
            if bishop_number[index_number] < bishop_count:
                bishop_number[index_number] = bishop_count
        else:
            backtracking(input_chess, bishop_count, idx + 1, index_number)
        if bishop_number[index_number] < bishop_count:
            bishop_number[index_number] = bishop_count

    backtracking(black_coordinate, 0, 0, 0)
    black_count = bishop_number[0]
    backtracking(white_coordinate, 0, 0, 1)
    white_count = bishop_number[1]
    return black_count + white_count


print(main(input_chess))
