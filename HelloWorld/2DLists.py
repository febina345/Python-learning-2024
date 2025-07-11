matrix=[
    [1 ,2, 3],
    [4 ,5 ,6],
    [6 ,7 ,8]
]

for row in matrix:
    for item in row:
        print(item)
matrix[0][1]=20

print(matrix[0][1])