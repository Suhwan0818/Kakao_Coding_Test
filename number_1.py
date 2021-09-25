from bisect import bisect_left
from itertools import combinations

def make_all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))

        for key in all_people.keys():
            all_people[key].sort()

        for q in query:
            seperate_q = q.split()
            target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
            if target in all_people.keys():
                answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo = 0, hi = len(all_people[target])))
            else:
                answer.append(0)

        return answer