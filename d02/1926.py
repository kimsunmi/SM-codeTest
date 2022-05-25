T = int(input())
answer = ""
for test_case in range(1, T):
    answer += '-' * (str(test_case).count('3') + str(test_case).count('6') +str(test_case).count('9')) if '3' in str(test_case) or '6' in str(test_case) or '9' in str(test_case) else str(test_case)
    answer += " "
 
answer += '-' * (str(T).count('3') + str(T).count('6') +str(T).count('9')) if '3' in str(T) or '6' in str(T) or '9' in str(T) else str(T)
 
print(answer)
