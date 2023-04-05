txt="the sun rises in the east".split()
print(txt)
vocab=["sun","in","east","doctor","day"]
res=[]
for i in txt:
    if i not in vocab and i not in res and i!=" ":
        res.append(i)
if len(res)==0:
    res=-1
print(res)