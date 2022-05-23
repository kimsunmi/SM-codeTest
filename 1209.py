for __ in range(10):
    test_case = input()
    list_ = [list(map(int,input().split())) for __ in range(100)]
    sum_list = []
    
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += list_[i][j]
        sum_list.append(sum)
     
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += list_[j][i]
        sum_list.append(sum)
         
    sum_list = sorted(sum_list,reverse = True)
     
    print("#{} {}".format(test_case,sum_list[0]))
