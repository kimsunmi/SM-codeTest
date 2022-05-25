for __ in range(0, 10):
    test_case = input()
    data_list = list(map(int,input().split()))

    i = 1
    while True:
        data_list[0] = data_list[0] - i
        data_list.append(data_list.pop(0))
        i = 1 if i + 1 == 6 else i + 1
        if data_list[-1] <= 0:
            data_list[-1] = 0
            break


    print("#" + str(test_case) + " " + " ".join(list(map(str,data_list))))
