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


def main(input_chess):
    result = []
    col_location = [-1] * len(input_chess)
    diag1 = [-1] * len(input_chess) * 2
    diag2 = [-1] * len(input_chess) * 2
    max_count = [-1]

    def backtracking(row, count):

        for i in range(len(input_chess)):
            if max_count[0] < count:
                max_count[0] = count
            if (
                (col_location[i] != 1)
                # and (diag1[row + i] != 1)
                # and (diag1[row - i + len(input_chess)] != 1)
                and input_chess[row][i] == 1
            ):
                col_location[i] = 1
                diag1[row - i + len(input_chess)] = 1
                diag1[row + i] = 1
                count += 1
                backtracking(row + 1, count)
                col_location[i] = -1
                diag1[row - i + len(input_chess)] = -1
                diag1[row + i] = -1
                count -= 1

    backtracking(0, 0)
    return max_count


print(main(input_chess)[0])
