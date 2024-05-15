def solution(num_list):
    answer = 0
    if len(num_list) > 10 :
        answer = sum(num_list)
    else :
        t = 1
        for i in num_list:
            t *= i 
        answer = t
            
    return answer