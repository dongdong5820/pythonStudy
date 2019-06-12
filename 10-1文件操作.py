#coding:utf-8

fo = open('foo.txt', 'w')
fo.write('www.runoob.com!\nVery good site!\n')
seq = ['菜鸟教程1\n','菜鸟教程2\n']
fo.writelines(seq)
fo.close()
print('文件写入成功！')
