for test_case in range(10):
    wid = int(input())
    buildings = list(map(int,input().split()))
     
    sum = 0
    for index in range(2, wid-2):
        RL_buildings = sorted(buildings[index-2:index]+buildings[index+1:index+3], reverse = True)
        sum += buildings[index] - RL_buildings[0] if buildings[index] - RL_buildings[0] >0 else 0
 
    print("#{} {}".format(test_case+1,sum))
