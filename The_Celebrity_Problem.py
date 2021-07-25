# Problem Statement

# A celebrity is a person who is known to all 
# but does not know anyone at a party. 
# If you go to a party of N people, find if there is a celebrity in the party or not.

import numpy as np

def celebrity():
    n = int(input("Enter the number of people"))
    matrix = []

#Get the number of people
    for i in range(n):
        a = []
        for j in range(n):
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
                ans = i
            elif count==n:
                return ans
    return ans
                
#Check if the valid input is been taken
def check(k):
    if(k==0 or k==1):
        return k
    else:
        print("Invalid param")
        k = int(input())
        check(k)


ans = celebrity()
print(ans)


# Output
# Enter the number of people 3
# 0
# 1
# 0
# 0
# 0
# 0
# 1
# 0
# 0

# 0 1 0  
# 0 0 0 
# 1 0 0 

# 1


# Explanation : Person 1 doesn't know anyone. Therefore, 1 is the celebrity


# Enter the number of people2
# 1
# 0
# 0
# 1
# 1 0 
# 0 1 
# -1

# Nobody is celebrity

