# rotate90degreePrint
def rotate90degreePrint(M):
    N=len(M)
    for j in range(N) :
        for i in range(N - 1, -1, -1) :
            print(M[i][j], end = "  ")
        print("")
        
# taking balls as +ve numbers (greater than 0) and -1 as empty space
# input matrix should be square
def rotate90degreeBallDropDown(M):
    N=len(M)
    # initialize new matrix
    NM = [[0 for i in range(N)]for j in range(N)]

    for j in range(N - 1, -1, -1) : #loop from bottom right corner
        for i in range(N - 1, -1, -1) :
            if M[i][j] == -1:
                for tj in range(j-1,-1,-1):
                    if(M[i][tj] >-1):
                        NM[j][N-i-1] = M[i][tj]
                        M[i][tj] = -1
                        break
            else:
                if NM[j][N-i-1] > -1:
                    NM[j][N-i-1]=M[i][j]

    printMatrix(NM)
    
# print any 2D - Util function
def printMatrix(M):
    for r in M:
        for c in r:
            print(c,end = " ")
        print("\n")
    

# Note : Square matrix
M = [[1,-1,-1,-1],[2,3,-1,-1],[4,5,6,7],[8,9,10,11]]
# M = [[99,-1,-1,-1,-1],[82,73,33,-1,-1],[64,55,46,37,31],[28,19,10,11,24],[18,91,20,51,74]]
printMatrix(M)
# print("\n********************")
# print("********************\n")
# rotate90degreePrint(M)
print("\n********************")
print("********************\n")
rotate90degreeBallDropDown(M)

# *************************
# Output of above script 
# *************************\

# *********INPUT Matrix***********
# 1 -1 -1 -1 
# 2 3 -1 -1 
# 4 5 6 7 
# 8 9 10 11 
# *********OUTPUT Matrix***********
# 8 4 0 0 
# 9 5 0 0 
# 10 6 2 0 
# 11 7 3 1 

