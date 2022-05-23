day_30 = ["4","6","9","11"]
day_31 = ["1","3","5","7","8","10","12"]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_date = input()
    year = input_date[:4]
    month = input_date[4:6]
    day = input_date[6:]
     
    if int(month) < 1:
        print("#" + str(test_case) + " " + "-1")
        continue
    if month == "02":
        if int(day) >28:
            print("#" + str(test_case) + " " + "-1")
            continue
    if month in day_30:
        if int(day) > 30:
            print("#" + str(test_case) + " " + "-1")
            continue
    if month in day_31:
        if int(day) > 31:
            print("#" + str(test_case) + " " + "-1")
            continue
     
    print("#" + str(test_case) + " " + year + "/" + month + "/" + day)
        

