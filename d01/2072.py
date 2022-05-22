T = int(input())
for test_case in range(1, T + 1):
    sum=0
    N=list(map(int,input().split(" ")))
    for k in N:
        if k%2 != 0:
            sum+=k
    print("#{} {}".format(test_case,sum))
