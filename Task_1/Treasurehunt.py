a = [[34,21,32,41,25],[14,42,43,14,31],[54,45,52,42,23],[33,15,51,31,35],[21,52,33,13,23]]

print(" visited:")
row=1
col=1
while True:
    curr= a[row-1][col-1]
    print(" visited",curr)
    if curr== 10*row+col:
        print("treasure at", curr)
        break
        
    row= curr//10
    col= curr%10
    