# # # #
# # # # import math
# # # #
# # # #
# # # import numpy
# # # # 7是分成几个小的列表
# # # chepai = ['京J9888','京J444','京J333','京J111','京J222']
# # # city = ['北京','河北']
# # # nu1m = len(chepai)/len(city)
# # # num = round(nu1m)
# # # a = numpy.array_split(chepai,(num,))
# # # print(a)
# # #
# # # # chepai = ['京J9888','京J444','京J333','京J111','京J222']
# # # # city = ['北京','河北']
# # # # nu1m = len(chepai)/len(city)
# # # # num = round(nu1m)
# # # #
# # # # for i in range(len(city)):
# # # # 	for j in range(i*num,num*(i+1)):
# # # # 		if len(chepai[j])-1>0:
# # # # 			print(chepai[j])
# # # # 			print(city[i])
# # # #
# # # #
# # # # #var arrtemp=[1,2,3,4]
# # # # # var city=[1,2,3,4]
# # # # # var _abs=parseInt(arrtemp.length/city.length)
# # # # # var _arrResult={}
# # # # # for(var i=0;i<city.length;i++)
# # # # # {
# # # # #    _arrResult["item"+i]=[];
# # # # #    var size=i!=city.length-1?(i+1)*_abs:arrtemp.length
# # # # #    for(var f=i*_abs;f<size;f++)
# # # # #    {
# # # # #       _arrResult["item"+i].push(arrtemp[f])
# # # # #    }
# # # # # a = [1,2,3,4,5,6,7,8,9,10]
# # # # # step = [1,2]
# # # # # c = len(a)/len(step)
# # # # # for i in range(len(a),c):
# # # # #     b = [a[i:i+c]]
# # # # #     print(b)
h = ''
hh = 0
hhh = 130255555555555555

lis = {}
lis.update(h1=h,h2=hh,h3=hhh)
for i, values in lis.items():
    if i == 'h1':
        if values == '' or values == 0:
            lis.update(h1='张三')
    elif i == 'h2':
        if values == '空' or values == 0:
            lis.update(h2=1)
    elif i == 'h3':
        if values == '空' or values == 0:
            lis.update(h3=666666666666666)
    else:
        print("没有")
print(lis)
# a1 = {'a':h, 'b':hh, 'c':''}
# b = [key for key, value in a1.items()]
# for i in range(0, len(a1)):
#     if a1[b[i]] == '':
#         if b[i] == 'a':
#             a1[b[i]] = 1
#         elif b[i] == 'c':
#             a1[b[i]] = 2
#     print(b[i])
#     print(a1[b[i]])
# #
#
#
#
# x = 'nihao'
#
# def func():
#     global x
#     x = 'nihao'
#
# func()
# print(x)
