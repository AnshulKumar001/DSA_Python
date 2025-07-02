num=[1,3,4,6,6,4,2,1,5,6,4,3]

dict1={}

for i in range (0,len(num)):
    if num[i] in dict1 :
        dict1[num[i]]+=1
    else:
        dict1[num[i]]=1
print(dict1)          