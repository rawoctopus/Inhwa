'''
2019.08.31
Inhwa Kwak
https://programmers.co.kr/learn/courses/30/lessons/17682
'''


def solution(dartResult):
    answer = 0
    num = ''
    score = []
    count = 0

    for cmd in dartResult:
        if cmd.isnumeric():
            num += cmd
            count += 1

        elif cmd == 'S':
            score.append(int(num) ** 1)
            num = ''
        elif cmd == 'D':
            score.append(int(num) ** 2)
            num = ''
        elif cmd == 'T':
            score.append(int(num) ** 3)
            num = ''

        elif cmd == '*':
            if count == 1:
                score[count-1] *= 2
            else:
                score[count-2] *= 2
                score[count-1] *= 2
        elif cmd == '#':
            score[count-1] *= -1
    
    answer = sum(score)
    
    return answer