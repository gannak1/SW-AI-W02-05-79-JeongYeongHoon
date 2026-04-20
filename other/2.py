import sys

input = sys.stdin.readline
channel = input().strip()
number_of_mal = int(input().strip())
if number_of_mal == 0: 
  mal_num = []
else:
  mal_num = list(map(int,input().strip().split()))

upper_number = 0
lower_number = 0
answer = []
for num in range(len(channel)):
  1

print(min((int(channel) - upper_number), (int(channel) - lower_number)) + len(channel))