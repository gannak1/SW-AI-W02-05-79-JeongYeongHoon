# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

"""
y좌표 상태 리스트,대각선 상태 리스트를 만들어서 y좌표, 대각이 겹치는지 확인하고 좌표를 단순하게 row를 재귀함수에서 +1하면서 앞으로 가되 나머지 col은 for문으로 모두 scope
backtracking으로서 대각선 y좌표 상태를 확인하고 모두 맞고 내려간 개수가 같으면 count를 +=1 해서 리턴

"""

max_number = int(input())


def main(N):

    col_position = [-1] * N  # 퀸의 세로 위치
    diag1 = [-1] * 2 * N  # 퀸이 존재하는 대각선 1 위치
    diag2 = [-1] * 2 * N  # 퀸이 존재하는 대각선 2 위치
    total_count = 0  # 경우의 수

    def dfs(row, total_count, select_count):
        if select_count == N:  # 퀸의 위치가 모두 놓일 경우 (리턴 정보)
            total_count += 1  # 경우의 수 1 추가
            return total_count
        if row == N:
            return total_count  # 최대 놓을 수 있는 개수가 초과하면 다시 원래대로 (index error 방지)
        for i in range(N):
            if (
                col_position[i] == -1  # 세로 위치에 없으면
                and diag1[row - i + N] != 1  # 대각선 1 위치에 없으면
                and diag2[row + i] != 1  # 대각선 2 위치에 없으면
            ):
                diag1[row - i + N] = 1  # 대각선 위치에 있다고 표시
                diag2[row + i] = 1  # 대각선 위치에 있다고 표시
                col_position[i] = 1  # 세로 위치에 있다고 표시
                total_count = dfs(row + 1, total_count, select_count + 1)  # 다음으로
                col_position[i] = -1  # 세로 위치에 없다고 표시
                diag1[row - i + N] = -1  # 대각선 위치에 없다고 표시
                diag2[row + i] = -1  # 대각선 위치에 없다고 표시
        return total_count

    total_count = dfs(0, total_count, 0)
    return total_count


print(main(max_number))
