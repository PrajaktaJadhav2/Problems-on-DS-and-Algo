import numpy as np

def celebrity():
    n = int(input("Enter the number of people"))
    matrix = []

#Get the number of people
    for i in range(n):
        a = []
        for j in range(n):
            if i==j:
                a.append(0)  #A person knows himself
            k = int(input())
            val = check(k)
            a.append(val)
        matrix.append(a)

    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

    ans = -1
    for i in range(n):
        count = 0
        for j in matrix[i]:
            if j == 0 :
                count = count + 1
            else:
                break
            if count==n and ans == -1:
                print(i)
            elif count==n:
                return -1
                


#Check if the valid input is been taken
def check(k):
    if(k==0 or k==1):
        return k
    else:
        print("Invalid param")
        k = int(input())
        check(k)


celebrity()
