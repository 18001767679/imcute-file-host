import turtle
wn=turtle.Screen()
grids=list(map(lambda x:list(map(lambda x:list("00000000000000000000000000000000"),range(32))),range(64)))
idx=0
x=0
with open("compiled","r")as a:
    for i in a.read().replace("v3.0 hex words plain\n","").split():
        grids[idx][31-x]=list(reversed(bin(int(i,16))[2:].zfill(32)))
        x+=1
        if x==32:
            x=0
            idx+=1
idx=0
turtle.pu()
def fxn(x,y):
    grids[idx][int(y/10)][int(x/10)+1]=str(1-int(grids[idx][int(y/10)][int(x/10)+1]))
    with open("compiled","w")as a:
        a.write("v3.0 hex words plain\n")
        lynz=0
        for i in grids:
            if not i:
                continue
            for j in reversed(i):
                a.write(hex(int("".join(reversed(j)),2))[2:].zfill(8))
                lynz+=1
                a.write(" " if lynz%8 else "\n")
def draw():
    turtle.clear()
    for jndex,j in enumerate(grids[idx]):
        for index,i in enumerate(j):
            turtle.goto(index*10,jndex*10)
            turtle.color("green" if i=="1" else "black")
            turtle.begin_fill()
            for s in range(4):
                turtle.left(90)
                turtle.forward(10)
            turtle.end_fill()
    turtle.ontimer(draw,1)
    
def less():
    global idx
    idx-=1
def more():
    global idx
    idx+=1
cpy=[]
def copy():
    global cpy
    cpy=list(map(lambda x:x[:],grids[idx][:]))
def paste():
    if cpy:
        grids[idx]=cpy
turtle.tracer(False)
wn.onclick(fxn)
wn.onkey(less,"a")
wn.onkey(more,"d")
wn.onkey(copy,"c")
wn.onkey(paste,"v")
wn.listen()
turtle.ontimer(draw,1)
turtle.done()
