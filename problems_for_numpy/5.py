import numpy as np

s = "adsqwexzs"

def f(s):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    part_1 = ""
    sub_s1 = ""
    sub_s2 = ""
    sub_s3 = ""
    if len(s) == 9 and s.islower():
        for i in range(9):
            if 0 <= i <= 2:
                sub_s1 += s[i]
            elif 3 <= i <= 5:
                sub_s2 += s[i]
            else:
                sub_s3 += s[i]
        
        for i in range(len(sub_s1)):
            for j in range (len(alph)):
                if i == 0 or i == 2:
                    if sub_s1[i] == alph[j]:
                        part_1 += str(j+1)
                else:
                    part_1 += sub_s1[i]
                    break

        part_2 = sub_s2[::-1]
        part_3 = ""

        for i in range(len(sub_s3)):
            for j in range(len(alph)):
                if sub_s3[i] == alph[j]:
                    if alph[j] == 'z':
                        part_3 += 'a'
                    else:
                        part_3 += alph[j + 1]

        return part_2 + part_3 + part_1
            
    else:
        return "BANG! BANG! BANG!"

print(f(s))
