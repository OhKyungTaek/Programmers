"""
Frist solve : 2021-01-05
"""
from collections import defaultdict
from copy import deepcopy

def solution(tickets):
    length = len(tickets) + 1
    answer = [0] * length
    sticket = sorted(tickets, key=lambda k: (k[0], k[1]))

    mydict = defaultdict(list)
    # Make Dictionary
    for i, j in sticket:
        mydict[i].append(j)

    # DFS
    def dfs(node, mdict, depth, ans):
        if(depth == length):
            ans[-1] = node
            return ans
        ans[depth-1] = node
        line = mdict[node]
        if(len(line) == 0) : return False
        for i in line:
            temp = deepcopy(mdict)
            temp[node].remove(i)
            res = dfs(i, temp, depth+1, ans)
            if not (res == False) : return ans
        return False

    return dfs('ICN', mydict, 1, answer)

if __name__ == '__main__':
    lastCase = [["ICN","C"],["ICN","B"],["C","ICN"],["B","D"]]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "SFO"], ["ATL", "ICN"]]

    result = solution(lastCase)
    print(result)
