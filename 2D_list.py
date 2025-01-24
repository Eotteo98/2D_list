import pgzrun

List = [[0,1,2],[3,4,5],[6,7,8]]


for i in range(len(List)):
    for j in range(len(List[0])):
        print(List[i][j], end="")
    print()

List2 = [[8,7,6],[5,4,3],[2,1,0]]

Sum = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(List)):
    for j in range(len(List[0])):
        Sum [i][j] = List [i][j]+List2 [i][j]
for _ in Sum:
    print(_)