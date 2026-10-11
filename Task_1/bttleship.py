import random
battle =[[0 for i in range(8)] for i in range(8)]

size=[6,4,2]



for length in size:
    placed = False
    while not placed:
        z=random.randint(0,1)
        #vertical
        if z==1: 
            x= random.randint(0,7)
            y=random.randint(0,8-length)   

            can = True
            for i in range(y,y+length):
                if battle[x][i]!=0:
                    can = False
                    break

                if can:
                    for i in range(y,y+length):
                        battle[x][i]=1
                    placed = True    

        else:

            x= random.randint(0,8-length)
            y=random.randint(0,7)
            can = True

            for i in range(x, x+length):
                if battle[i][y]!=0:
                    can = False
                   
                    break

                if can:
                    for i in range(x,x+length):
                        battle[i][y]=1
                    placed=True    

for i in range(8):
    print(battle[i])
                                    


while any(1 in row for row in battle):
    r=int(input("enter x coordinate"))
    c=int(input("ernter y coordinate"))
    if battle[r][c] == 1:
        print("hit")
        battle[r][c]=0
    else:
        print("miss")    
print("you win")          


            
          

        

    