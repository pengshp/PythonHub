#!/usr/bin/python3

#汉诺塔问题
def move(n,a,b,c):
    if n==1:
        print("%s --> %s"%(a,c))#the basic situation
    else:
        move(n-1,a,c,b)#move the n-1 from a to b
        move(1,a,b,c)#now,a has just one dish,so just move it to c
        move(n-1,b,a,c)#now,move the n-1 dishes from b to c

if __name__ == '__main__':
    move(3,"A","B","C")


def move(n, a, b, c):
    if n==1:
#如果只有一个盘子，直接移动到C上面；
        print('move', a, '-->', c)
        return
    else:
#将A上面N-1的盘子利用C移到B：
        move(n-1, a, c, b)
#将A最下面的1个盘子移到C：
        move(1, a, b, c)
#将B中的n-1个盘子利用A移到C上面：
        move(n-1, b, a, c)
        return
