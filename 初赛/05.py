# n = int(input())
# edges = []
# for i in range(n-1):
#     temp = input()
#     temp = temp.split(' ')
#     temp = [int(temp[i])-1 for i in range(len(temp))]
#     edges.append(temp)
# print(edges)
n = 4
edges = [[0, 1], [1, 2], [2, 3]]


color = [0 for i in range(n)]  # 0:无色,1:红色,2:蓝色
con = [[] for i in range(n)]
for edge in edges:
    con[edge[0]].append(edge[1])
    con[edge[1]].append(edge[0])

# 0,1同色
color[0] = 1
color[1] = 1


