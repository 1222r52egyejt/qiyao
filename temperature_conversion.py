
#华氏度转换为摄氏度
#获取华氏度
f = float(input('请输入华氏温度'))
#计算
c = (f - 32)/1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

#摄氏度转换为华氏度
#获取华氏度
c = float(input('请输入摄氏温度'))
#计算
f = c*1.8 + 32
print('%.1f摄氏度 = %.1f华氏度' % (c, f))