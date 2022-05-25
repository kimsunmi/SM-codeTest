from collections import Counter
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_num = input()
    numbers = list(map(int, input().split()))
    numbers_count = Counter(numbers).most_common()
     
    max_count = numbers_count[0][1]
    answer = numbers_count[0][0]
    if answer == numbers_count[1][1]:
        print(answer)
        for num_case in numbers_count:
            print(num_case)
            if num_case[1] < max_count:
                break
            if num_case[0] > answer:
                answer = num_case[0]
     
    print("#" + str(test_case) + " " + str(answer))
