'''
矩阵算法 (空间换时间,一维升二维)
参考： https://www.cnblogs.com/huxianglin/p/5995649.html
'''
'''
矩阵乘积：只有第一个矩阵列数和第二矩阵行数相同时乘积才有意义。
A(2*3) = [
	a11,a12,a13
	a21,a22,a23
]
B(3*2) = [
	b11,b12
	b21,b22
	b31,b32
]
C(2*2) = A*B = [
	a11*b11+a12*b21+a13*b31, a11*b12+a12*b22+a13*b32
	a21*b11+a22*b21+a23*b31, a21*b12+a22*b22+a23*b32
]
'''
import time
# 普通算法
def normal(n):
	a,b,c = 0,1,1
	while n:
		a,b,c = b,c,b+c
		n -= 1
	return a

# 计算二阶矩阵相乘
def multi(a,b):
    # 定义一个空的二阶矩阵
    c = [[0,0],[0,0]];
    for i in range(2):
        for j in range(2):
            for k in range(2):
				# 新二阶矩阵值的计算
                c[i][j] = c[i][j] + a[i][k]*b[k][j]
    return c

def matrix(n):
	# 元矩阵，可看做是2**0=1
	base = [[1,1],[1,0]]
	# 结果矩阵，相当于1。这个矩阵和任意二阶矩阵A的乘积还是A
	ans = [[1,0],[0,1]]
	while n:
		# n的二级制最后一位和1做与运算，若为1，就进去if体
		if n&1:
			ans = multi(ans,base)
		base = multi(base,base)
		# n的二进制往右移一位
		n>>=1
	# 最后获取二阶矩阵的[0][1]即f(n)的值
	return ans[0][1]

def main():
	n = int(input(">>>"))
	start = time.time()
	print("Normal:", normal(n))
	print("used:", time.time() - start)
	start = time.time()
	print("Matrix:", matrix(n))
	print("used:", time.time() - start)

main()