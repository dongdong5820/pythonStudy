"""
冒泡排序
    1、从当前元素起，向后依次比较每一对相邻元素，若逆序就交换
    2、对所有元素均重复以上步骤，直至最后一个元素
    举例: sList = [5,1,4,8,2]
    第一次: [1,4,5,2,8]    比较4次
    第二次: [1,4,2,5,8]    比较前3次
    第三次: [1,2,4,5,8]    比较前2次
    第四次: [1,2,4,5,8]    比较前1次
"""
def myBubbleSort(sList):
    length = len(sList) # 序列个数
    for i in range(length-1):       # 外循环为排序趟数(length-1)
        for j in range(length-i-1): # 内循环为每趟比较次数,第i趟比较length-i次
            if sList[j] > sList[j+1]:
                sList[j],sList[j+1] = sList[j+1],sList[j]
    return sList

myList = [5,1,12,4,8,2]
print(myBubbleSort(myList))
