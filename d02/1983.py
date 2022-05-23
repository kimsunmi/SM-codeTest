from math import ceil
 
T = int(input())
 
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for test_case in range(1, T + 1):
    score_dic = {}
    N, K = map(int,input().split())
    for i in range(N):
        mid, fin, rep = map(int,input().split())
        score_dic[i] = mid*0.35 + fin * 0.45 + rep * 0.2
         
    score_list = sorted(score_dic.items(), key = lambda x : x[1], reverse = True)
    for i in range(len(score_list)):
        if score_list[i][0] == K-1:
            print("#" + str(test_case) + " "+ grade[ceil((i+1)/N * 10) -1])
            break
