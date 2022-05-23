T = int(input())
 
for test_case in range(1,T+1):
    sum = 0
    num_list = list(map(int,input().split()))
    for num in num_list:
        if num % 2 != 0:
            sum += num
    print("#" + str(test_case) + " " + str(sum))
