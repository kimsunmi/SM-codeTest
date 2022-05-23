import sys
sys.stdin = open("../input.txt", "r")
T=10
for test_case in range(1,T+1):
    t=int(input())
    answer=0
    buildingList=list(map(int,input().split()))
    for i in range(2,t-2):
        m2=buildingList[i-2]
        m1=buildingList[i-1]
        p1=buildingList[i+1]
        p2=buildingList[i+2]
        allcase=[m2,m1,p1,p2]
        k=buildingList[i]-max(allcase)
        if (k>0):
            answer+=k
        else: continue
    
    print("#{} {}".format(test_case,answer))
