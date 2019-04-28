#根据用户输入的数字，输出正等边三角形
while True :
	num = input("请输入一个正整数：")
	if num.isdigit() and int(num) > 0 : 
		num = int(num)
		break
i = 1
while i <= num:
	x = 1
	while x <= (num - i):
		print(' ', end = '') 
		x += 1
	y = 1
	while y <= i:
		print('* ', end = '')
		y += 1
	print('')
	i += 1 
print('正等边三角形输出完成！！！')
