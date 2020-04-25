# 根据用户输入的数字，输出矩形
while True:
    num = input("请输入一个正整数：")
    if num.isdigit() and int(num) > 0:
        num = int(num)
        break

i = 1
while i <= num:
    j = 1
    while j <= num:
        print("*", end='')
        j += 1
    print()
    i += 1
print("矩形输出完成!!!")
