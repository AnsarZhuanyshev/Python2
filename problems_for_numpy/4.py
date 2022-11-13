import numpy as np

lst1 = ([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]],2)
lst2 = ([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
lst3 =  ([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)

def freq_count(lstd):
    def depth(lstd, dep_arr = [], others = [], dep = 0):
        lst = lstd[0]
        for i in lst:
            if type(i) == type(1):
                dep_arr.append([dep,int(i)])            
            
            else:
                for elements in i:
                    others.append(elements)
        
        if len(others) == 0:
            nums,arr,k =[],dep_arr,lstd[1]

            for i in arr:
                if i[1]==k:
                    nums.append(i)
            maxi = arr[-1][0]
            output = [[i,0] for i in range(maxi+1)]

            for i in nums:
                output[i[0]][1]+=1
            return output

        else:
            lst, others, dep = [others,lstd[1]], [], dep+1
            return depth(lst,dep_arr,others,dep)
    
    return depth(lstd)

print(freq_count(lst1))
print(freq_count(lst2))
print(freq_count(lst3))