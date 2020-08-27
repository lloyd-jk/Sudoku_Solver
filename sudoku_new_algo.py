import os
import time
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
        

def sudoku_finish():
    for x in sudoku_input:
        for y in x:
            if y == 0:
                return True
    return False

def row_col_check(no,rno,cno):
    # print('no',no,'row',rno,'col',cno)
    for x in sudoku_input[rno]:
        # print('row ele',x)
        if x == no:
            return False
    for x in range(0,9):
        # print('col ele',sudoku_input[x][cno])
        if sudoku_input[x][cno]==no:
            return False
    return True

def check_box(x1,index):
    for x,y in index:
        if sudoku_input[x][y]==x1:
            return False
    return True


            
def check_values(index):
    # finished=[]
    for x in range(1,10):
        count=0
        if check_box(x,index):
            for y in index:
                if sudoku_input[y[0]][y[1]]==0:
                    if row_col_check(x,y[0],y[1]):
                        count+=1
                        r=y[0]
                        c=y[1]
            if count==1:
                sudoku_input[r][c]=x

def check_box_fin(x):
    for y in x:
        if y == 0:
            return False
    return True
#------------------------------------------
def find_emptybox():
    for x in range(1,10):
        for y in range(1,10):
            if sudoku_input[x][y]==0:
                return (x,y)
    return False

def check_ass(x,position):
    for x in sudoku_input[position[0]]:
        if x == no:
            return False
    for x in range(0,9):
        if sudoku_input[x][position[1]]==no:
            return False
    for x,y in position:
        if sudoku_input[x][y]==x1:
            return False
    return True

def assigning(position):
    for x in range(1,10):
        check_ass(x,position)

def run():
    while True:
        position=find_emptybox(x)
        assigning(position)
        if not position:
            break


      

             


box_indexes=[
    [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
    [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
    [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
    [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
    [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
    [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
    [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
    [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
    [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)],
    ]

sudoku_input=[[0]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9]
# ------------------------
sudoku_input[0]=[0,0,0, 6,0,0, 4,0,0]
sudoku_input[1]=[7,0,0, 0,0,3, 6,0,0]
sudoku_input[2]=[0,0,0, 0,9,1, 0,8,0]

sudoku_input[3]=[0,0,0, 0,0,0, 0,0,0]
sudoku_input[4]=[0,5,0, 1,8,0, 0,0,3]
sudoku_input[5]=[0,0,0, 3,0,6, 0,4,5]

sudoku_input[6]=[0,4,0, 2,0,0, 0,6,0]
sudoku_input[7]=[9,0,3, 0,0,0, 0,0,0]
sudoku_input[8]=[0,2,0, 0,0,0, 1,0,0]
run()
# ------------------
# sudoku_input[0]=[1,0,0, 4,8,9, 0,0,6]
# sudoku_input[1]=[7,3,0, 0,0,0, 0,4,0]
# sudoku_input[2]=[0,0,0, 0,0,1, 2,9,5]

# sudoku_input[3]=[0,0,7, 1,2,0, 6,0,0]
# sudoku_input[4]=[5,0,0, 7,0,3, 0,0,8]
# sudoku_input[5]=[0,0,6, 0,9,5, 7,0,0]

# sudoku_input[6]=[9,1,4, 6,0,0, 0,0,0]
# sudoku_input[7]=[0,2,0, 0,0,0, 0,3,7]
# sudoku_input[8]=[8,0,0, 5,1,2, 0,0,4]



