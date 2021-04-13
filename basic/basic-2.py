# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，
# 就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
print('ABC'.encode('ascii')) #   b'ABC'
print('中文'.encode('utf-8')) #  b'\xe4\xb8\xad\xe6\x96\x87'

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#len()字符串长度,len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('123ABc!'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) #1中文3字节

#格式化
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#format(),传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string:f''
# 它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r=1.2
s=r*r
print(f'The area of a circle with radius {r} is {s:.2f}')

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print(f'小明成绩提高百分比：{r:.1f}%')


