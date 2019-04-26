#根据用户输入正整数N，求N的阶乘
def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n-1)

def main():
	while True:
		num = input("请输入一个正整数：")
		if num.isdigit() and int(num) > 0:
			num = int(num)
			break
	print('%s的阶乘为%s'%(num, factorial(num)))

main()
	



