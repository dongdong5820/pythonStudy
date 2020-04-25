# 根据用户输入数字N，输出斐波拉契数列前N项
# 斐波拉契数列特点： f(n) = f(n-1) + f(n-2), 如1,1,2,3,5,8,13,21...

# 2n次递归，随着递归深度加深，效率直线下降
def fn(n):
    if n <= 2:
        return 1
    return fn(n - 1) + fn(n - 2)

# n次递归，效率稍好
def goodFn(n,pre=1,cur=1):
    if n <= 2:
        return cur
    pre,cur = cur,pre + cur
    return goodFn(n-1,pre,cur)

# 循环方式-while
def whileFn(n):
    a,b,c = 0,1,1
    while n:
        a,b,c = b,c,b+c
        n -= 1
    return a

# 矩阵算法，请参考 05-2斐波拉契(矩阵算法).py

# 主函数


def main():
    while True:
        num = input("请输入一个正整数：")
        if num.isdigit() and int(num) > 0:
            num = int(num)
            break
    i = 1
    list = []
    while i <= num:
        #list.append(fn(i))
        #list.append(goodFn(i))
        list.append(whileFn(i))
        i += 1
    print('斐波拉契数列前%d项为%s' % (num, list))


main()
