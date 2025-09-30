from utils import IO as io
not_free=False
free=True
n=8
row=[free]*n
col=[free]*n
dpos=[free]*(2*n-1)
dneg=[free]*(2*n-1)

def backtracking(board,i):
    # 放置成功
    if i==n:
        for i in range(n):
            line=[]
            for j in range(n):
                if board[i][j]==False:
                    line.append(".")
                else:line.append("Q")
            print("".join(line))
        return
    if row[i]==not_free:
        backtracking(board,i+1)
        return
    # 从第0列开始尝试放
    for j in range(n):
        # 安全
        if  col[j]==not_free or dpos[i+j]==not_free or dneg[i-j+n-1]==not_free:
            continue
        # 放下皇后并更新数组
        board[i][j] = True
        row[i]=not_free
        col[j] = not_free
        dpos[i + j] = not_free
        dneg[i - j + n - 1] = not_free
        backtracking(board, i + 1)
        # 拿掉皇后 回溯
        row[i]=free
        col[j] = free
        dpos[i + j] = free
        dneg[i - j + n - 1] = free
        board[i][j] = False

def main():
    k=io.read_int()
    board=[[False for i in range(8)]for j in range(8)]
    for i in range(k):
        i=io.read_int()
        j=io.read_int()
        row[i]=not_free
        col[j]=not_free
        dpos[i+j]=not_free
        dneg[i-j+n-1]=not_free
        board[i][j]=True
    backtracking(board,0)

if __name__== "__main__":
    main()

