'''
2019.08.31
Inhwa Kwak
https://programmers.co.kr/learn/courses/30/lessons/17677
'''

def getSimil(str1_list, str2_list):
    intersection = []
    union = []
    similarity = 0

    for i in str2_list:
        if i in str1_list:
            intersection.append(i)

    union = str1_list + str2_list

    for i in intersection:
        if i in union:
            union.remove(i)

    if len(union) == 0:
        similarity = 1
        return int(similarity*65536)
    else:
        similarity = len(intersection)/len(union)
        return int(similarity*65536)



def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i] + str1[i+1])
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i] + str2[i+1])

    if len(str1_list) > len(str2_list):
        answer = getSimil(str1_list, str2_list)
    else:
        answer = getSimil(str2_list, str1_list)

    return answer