with open("photos.txt","r")as a:
    k=a.read().split("\n")
n=[]
for i in k:
    res=""
    for j in i:
        res+=j
        res+=j
    n.append(res)
    n.append(res)
with open("compiled","w")as a:
    a.write("v3.0 hex words plain\n")
    lynz=0
    catch=[]
    for i in n:
        if not i:
            continue
        a.write(hex(int(reversed(i),2))[2:].zfill(8))
        a.write(" " if lynz%8 else "\n")
        lynz+=1
        catch.append(i)
        if lynz%32==0:
            for j in catch:
                if not j:
                    continue
                a.write(hex(int(str(reversed(j)),2))[2:].zfill(8))
                a.write(" " if lynz%8 else "\n")
            catch=[]
        
