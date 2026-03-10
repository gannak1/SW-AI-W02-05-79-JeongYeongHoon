# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

"""
중간에 값 넣는 것

"""

input_text = input()


def function(input_text):  # 코드의 수를 줄이기 위해서 선언
    result = ""
    split_text = input_text.split(":")  # :로 분배
    for i in range(len(split_text)):  # 분배한 코드를 순회
        if i != len(split_text) - 1:  # 끝부분이 아닌 경우 nnnn에 : 추가
            result = result + ("000000" + split_text[i])[-4:] + ":"
        else:  # 끝부분인 경우 nnnn만 추가
            result = result + ("000000" + split_text[i])[-4:]
    return [result, len(split_text)]


if len(input_text.split("::")) > 1:  # ::로 분배한 것이 하나 이상이면
    count = 0
    blank_index = -1
    split_double_text = input_text.split("::")  # ::로 분배
    for i in range(len(split_double_text)):
        if split_double_text[i] != "":  # 비어 있지 않은 경우
            split_double_text[i], temp_count = function(
                split_double_text[i]
            )  # 자리를 얼마나 차지하는지 카운터하는 숫자와 변환한 string을 각각 받기
            count += temp_count  # 카운트에 추가
        else:  # 비어 있으면 나머지 숫자로 0으로 채울 예정
            blank_index = i  # 비어있는 인덱스 표시
    if blank_index == -1:  # 양쪽 모두 숫자가 있는 경우
        split_double_text.insert(
            1, ":".join(["0000" for i in range(8 - count)])
        )  # 카운트만큼 추가
    else:
        split_double_text[blank_index] = ":".join(
            ["0000" for i in range(8 - count)]
        )  # 남은 것만큼 추가
    result = ":".join(split_double_text)  # :로 합치기

else:
    result = function(input_text)[0]  # 기존 함수로 그대로 리턴
print(result)
