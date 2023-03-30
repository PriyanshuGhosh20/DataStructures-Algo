l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
l2.reverse()
l3=[]
for i in range(0,len(l1)):
    if l2[i]==None:
        l3+=[l1[i]+""]
    elif l1[i]==None:
        l3+=[l2[i]+""]
    else:
        l3+=[l1[i]+l2[i]]
print(*l3)