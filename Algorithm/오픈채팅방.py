'''
2019.07.27
Inhwa Kwak
https://programmers.co.kr/learn/courses/30/lessons/42888
'''

def solution(record):
    answer = []
    uidNick = {}
    
    for line in record:
        splitData = line.split(" ")
        if splitData[0]=="Enter":
            uidNick[splitData[1]] = splitData[2]
        if splitData[0]=="Change":
            uidNick[splitData[1]] = splitData[2]
      
    for line in record:
        splitData = line.split(" ")
        if splitData[0]=="Enter":
            answer.append(uidNick[splitData[1]]+"님이 들어왔습니다.")
        if splitData[0]=="Leave":
            answer.append(uidNick[splitData[1]]+"님이 나갔습니다.")
            
    return answer