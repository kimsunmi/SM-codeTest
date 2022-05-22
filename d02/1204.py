import sys
sys.stdin = open("input.txt", "r")
# 위 두줄 제외하여 컴파일 필

T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    number=0
    highOverlap=0
    highScore=0
    test_result=0
    scoreList = list(map(int, input().split()))
    arangeScoreList = list(set(scoreList))

    for i in arangeScoreList:
        number = scoreList.count(i)
        if highOverlap < number or (highOverlap == number and highScore < number*i):
            test_result=i
            highOverlap=number
            highScore=number*i
    print("#{} {}".format(t,test_result))
