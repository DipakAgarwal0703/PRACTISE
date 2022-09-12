n=int(input("Enter the number of matrix:"))
if (n%2!=0):
    MS=[[0 for x in range(n)]
        for y in range (n)]

    i=n//2
    j=n-1

    num=1

    while (num<=(n * n)):
        if (i==-1 and j==n):
            j=n-2
            i=0

        else:
            if (j==n):
                j=0

            if (i<0):
                i=n-1

        if (MS[int (i)] [int (j)]):
            j=j-2
            i=i+1
            continue
        
        else:
            MS[int (i)][int (j)]=num
            num=num+1

        i=i-1
        j=j+1

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (MS[i][j]),
                  end='')

            if j==(n-1):
                print ()
else :
    print ("Enter odd value of n")
    
