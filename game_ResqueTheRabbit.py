# 2020-10-11
# Wang Xiaoming, wangxiaoming622@sina.com
# 问题描述：兔子每天吃一斤胡萝卜可以涨一斤，2斤青菜可以长2斤 18斤才有力气逃跑，
# 兔子每天可以选择吃一斤胡萝卜或者两斤青菜，
# 第一天开始有多少种不同的饮食方法可以成功逃出屠场，20斤就会被卖掉
# the answer is 10946
# self comments: 初学编程能力较弱，程序写得较low，期待以后更新！
#
###————————————————————————————
import itertools
from itertools import product
# list1 = []
# for i in product(range(1, 3), repeat=19):
#     list1.append(i)
#     print(i, file=ff)

# list0 = [i0 for i0 in product([1, 2], repeat=1)]
# print(list0)
list1 = [i for i in product([1, 2], repeat=9) if sum(i) in range(18, 20)]       # 等价代码 list1 = [i for i in product(range(1, 3), repeat=19)]
print('数目：', len(list1))
list2 = [i for i in product([1, 2], repeat=10) if sum(i) in range(18, 20)]
print('数目：', len(list2))
list3 = [i for i in product([1, 2], repeat=11) if sum(i) in range(18, 20)]
print('数目：', len(list3))
list4 = [i for i in product([1, 2], repeat=12) if sum(i) in range(18, 20)]
print('数目：', len(list4))
list5 = [i for i in product([1, 2], repeat=13) if sum(i) in range(18, 20)]
print('数目：', len(list5))
list6 = [i for i in product([1, 2], repeat=14) if sum(i) in range(18, 20)]
print('数目：', len(list6))
list7 = [i for i in product([1, 2], repeat=15) if sum(i) in range(18, 20)]
print('数目：', len(list7))
list8 = [i for i in product([1, 2], repeat=16) if sum(i) in range(18, 20)]
print('数目：', len(list8))
list9 = [i for i in product([1, 2], repeat=17) if sum(i) in range(18, 20)]
print('数目：', len(list9))
list10 = [i for i in product([1, 2], repeat=18) if sum(i) in range(18, 20)]
print('数目：', len(list10))
list11 = [i for i in product([1, 2], repeat=19) if sum(i) in range(18, 20)]
print('数目：', len(list11))

answer = len(list1) + len(list2) + len(list3) + len(list4) + len(list5) + len(list6) + len(list7) + len(list8)\
      + len(list9) + len(list10) + len(list11)
print('Answer: ', answer)


# if __name__ == '__main__':

# import itertools
# nums = itertools.permutations([1, 2], 1)
# for x in nums:
#     print(x)

# L = [1, 2, 3]
# list = [x for x in L]
# print(list)

 # def main()
 #     sum = 0
 #     n = int()
 #     for x in range(n):
 #         sum

# ff = open('C:/Users/user2014/PycharmProjects/Practice/result.txt', 'w')
# ff.close()