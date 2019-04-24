#根据用户输入的数字，输出一个正直角三角形
while True :
	num = input("请输入一个正整数：")
	if num.isdigit() and int(num) > 0 : 
		num = int(num)
		break

i = 1
while i <= num :
	j = 1
	while j <= i :
		print("*", end = "")
		j+=1
	print()
	i+=1
print("正直角三角形输出完成！！！")
