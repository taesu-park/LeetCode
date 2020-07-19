#(2) Course Schedule II

def findOrder(numCourses,prerequisites):
    check = [[] for _ in range(numCourses)]
    visit = [0]*numCourses
    for i in range(len(prerequisites)):
        check[prerequisites[i][1]].append(prerequisites[i][0])
        visit[prerequisites[i][0]] += 1
    print(check,visit)
    zero = []
    for i in range(numCourses):
        if visit[i] == 0:
            zero.append(i)
    result = []
    while zero:
        tmp = zero.pop()
        result.append(tmp)
        for i in check[tmp]:
            visit[i] -= 1
            if visit[i] == 0:
                zero.append(i)
    return result if len(result) == numCourses else []
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))