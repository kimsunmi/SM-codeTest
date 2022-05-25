# 조건 : 재귀함수

def power(num, count):
    if count == 1:
        return num
    return power(num, count-1) * num

for __ in range(0, 10):
    test_case = input()
    data_list = list(map(int,input().split()))
    print(f"#{test_case} {power(data_list[0], data_list[1])}")
