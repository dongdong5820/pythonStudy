#根据用户输入数字N，输出汉诺塔数列集合

#输出汉诺塔的第N项
def fn(n):
	if n == 1:
		return 1
	return 2*fn(n-1)+1

def main():
	while True:
		num = input("请输入一个正整数：")
		if num.isdigit() and int(num) > 0 : 
			num = int(num)
			break
	i = 1
	list = []
	while i <= num:
		list.append(fn(i))
		i += 1
	print('汉诺塔数列前%d项为：%s'%(num,list))

main()
