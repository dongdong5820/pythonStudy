# 根据用户输入数字N，输出斐波拉契数列前N项

# 输出斐波拉契数据第N项


def fn(n):
    if n <= 2:
        return 1
    return fn(n - 1) + fn(n - 2)

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
        list.append(fn(i))
        i += 1
    print('斐波拉契数列前%d项为%s' % (num, list))


main()
