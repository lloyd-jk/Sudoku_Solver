def printer():
    count1=1
    count2=0
    print("| ",end="")
    for x in sudoku_input:
        for y in x:
            if count2%3==0 and count2!=0:
                print("| ",end="")
            print(y,end=" ")
            count2+=1
        print("")
        if count1%3==0 and count1!=0:
            print("- - "*6)
        count1+=1
        
def find_emptybox():
    for x in range(0,9):
        for y in range(0,9):
            if sudoku_input[x][y]==0:
                return (x,y)
    return False

def check_ass(x,position):
    for i in sudoku_input[position[0]]:
        if i == x:
            return False
            
    for i in range(0,9):
        if sudoku_input[i][position[1]]==x:
            return False

    var1 = position[0] // 3
    var2 = position[1] // 3

    for i in range(var1*3, var1*3 + 3):
        for j in range(var2 * 3, var2*3 + 3):
            if sudoku_input[i][j] == x and (i,j) != position:
                return False
    return True



def run():
    empty_indice=find_emptybox()

    if not empty_indice:
        return True

    for x in range(1,10):
        if check_ass(x,empty_indice):
            sudoku_input[empty_indice[0]][empty_indice[1]]=x

            if run():
                return True
            sudoku_input[empty_indice[0]][empty_indice[1]]=0
    
    return False



sudoku_input=[[0]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9]
# -----------------------------------
sudoku_input[0]=[8,0,0, 0,0,0, 0,0,0]
sudoku_input[1]=[0,0,3, 6,0,0, 0,0,0]
sudoku_input[2]=[0,7,0, 0,9,0, 2,0,0]

sudoku_input[3]=[0,5,0, 0,0,7, 0,0,0]
sudoku_input[4]=[0,0,0, 0,4,5, 7,0,0]
sudoku_input[5]=[0,0,0, 1,0,0, 0,3,0]

sudoku_input[6]=[0,0,1, 0,0,0, 0,6,8]
sudoku_input[7]=[0,0,8, 5,0,0, 0,1,0]
sudoku_input[8]=[0,9,0, 0,0,0, 4,0,0]
# --------------------------------------
run()
printer()




