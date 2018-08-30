lst = []
for i in range(32,128):
    if (i-2)%10 == 0:
        print()
        print(i,'-',chr(i), end = ' ')
    else:
        print(i,'-',chr(i),end = ' ')