for test_case in range(1, 11):
    T = int(input())
    buildingList=list(map(int, input().split()))
    for i in range(1,T+1):
        highB = max(buildingList)
        lowB = min(buildingList)
        if highB > lowB:
            idx=buildingList.index(highB)
            buildingList[idx]-=1
            idx=buildingList.index(lowB)
            buildingList[idx]+=1
    highB = max(buildingList)
    lowB = min(buildingList)
    print("#{} {}".format(test_case, highB-lowB))