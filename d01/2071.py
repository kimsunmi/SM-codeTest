T = int(input())
for test_case in range(1, T + 1):
    # 띄어쓰기로 입력값 리스트로 받아오기
    numberList=list(map(int, input().split()))
    # 리스트 한 행을 다 더한 변수
    answer=0
    # 10개씩 받아오므로 0-9까지 answer에 더하기
    for i in range(0,10):
        answer += numberList[i]
    # 소수 첫째자리에서 반올림하므로 평균 및 round 계산
    print("#{} {}".format(test_case,round(answer/10)))