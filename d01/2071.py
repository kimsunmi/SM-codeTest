#8m 20s

T = int(input())

for test_case in range(1, T + 1):
    print("#{} {}".format(test_case, round(sum(list(map(int,input().split())))/10)))
