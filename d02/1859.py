T = int(input())
for test_case in range(1, T + 1):
    leng = int(input())
    data = list(map(int,input().split()))
    point = 0
    pre_point = 0
    result = 0
    while len(data) > 0:
        point = data.index(max(data))
        result += data[point] * (point+1) - sum(data[:point+1])
        data = data[point+1:]
    print(f"#{test_case} {result}")
