import numpy 

arr2 = numpy.array([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]) 

def matrix(arr):
    len_columns = len(arr.T)
    
    new_arr = []
    for i in range(len(arr)+2):
        null = []
        for j in range(len_columns+2):
            null.append('0')
        new_arr.append(null)

    for i in range(len(arr)):
        for j in range(len_columns):
            if arr[i][j]=='#':
                for new_i in range(i, i+3):
                    for new_j in range(j, j+3):
                        new_arr[new_i][new_j]=int(new_arr[new_i][new_j])+1
                new_arr[i+1][j+1]='#'
    out = []
    for k in new_arr[1:-1]:
        out.append(k[1:-1] )
    new_new_arr = numpy.array(out)

    return new_new_arr

print(matrix(arr2))