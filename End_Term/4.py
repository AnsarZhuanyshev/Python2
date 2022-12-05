import numpy
big_mtx = [[0,0,0],
            [0,0,0],
            [0,0,0],
             [0,0,0],
            [0,0,0],
            [0,0,0],
             [4,0,0],
             [0,4,0],
            [0,0,4]]
all_matrices =[[] for i in range(len(big_mtx)//3)]
for i in range(len(big_mtx)):
    all_matrices[i//3].append(big_mtx[i])
print(all_matrices)

for j in all_matrices:
    print(numpy.matrix(j),"\n")