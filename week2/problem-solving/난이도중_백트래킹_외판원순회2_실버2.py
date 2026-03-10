# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

"""
dfs로 모든 경로를 탐색하여 비용 계산
"""

city_array = [list(map(int, input().split())) for i in range(int(input()))]


def main(city_cost):
    min_value = [9999999999999]  # 최소 값
    current_array = []  # 탐험한 도시 비용 순서 리스트
    departed_city = []  # 도착한 도시 순서 리스트

    def back_tracking(current_city):
        if len(current_array) == len(city_cost):  # 순회할 도시 수와 같으면
            if min_value[0] > sum(current_array):  # 값이 최소 값인 경우 값을 저장
                min_value[0] = sum(current_array)
            return
        for next_city in range(len(city_cost)):
            if current_city == next_city:  # 다음 도시와 현재 도시가 같으면 다음으로
                continue
            elif next_city in departed_city:  # 도착했던 도시에 있는 경우 다음으로
                continue
            elif (
                city_cost[current_city][next_city] == 0
            ):  # 도시 cost가 0일경우 다음으로 (진행안한다고 설명)
                continue
            elif (
                next_city == 0 and len(current_array) < len(city_cost) - 1
            ):  # 출발지가 마지막이 아닌 경우 취소
                continue
            elif (
                next_city != 0 and len(current_array) == len(city_cost) - 1
            ):  # 마지막이 출발지가 아닌 경우 취소
                continue
            else:
                current_array.append(city_cost[current_city][next_city])  # 코스트 추가
                departed_city.append(next_city)  # 다음 도시 예정지 추가
                back_tracking(next_city)  # 다음 도시로
                current_array.pop()  # 코스트 취소
                departed_city.pop()  # 도착지 취소

    back_tracking(0)
    return min_value  # 최소값 리턴


print(main(city_array)[0])
