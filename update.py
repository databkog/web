import sys,random



path=sys.path[0]+r'/0d.txt'
def cv(kitu):
    ds=[]
    ds[:0]=kitu
    return ds
keys=cv(custom)
mykey=""
nums=random.randint(5,20)    
for i in range(nums):
    key=keys[random.randint(0,len(custom)-1)]
    mykey=mykey+key
with open(path, 'w+') as f:
    f.write(mykey)
