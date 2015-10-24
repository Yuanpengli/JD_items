__author__ = 'liyuanpeng'
num =10



# while True:
#
#     nums=str(num)
#     numbers=list(nums)
#     l=len(numbers)
#
#     sum=0
#
#     for i in range(l):
#         sum = sum +int(numbers[i])
#
#     num = sum
#
#     if sum<10:break
# print sum

while True:

    nums = str(num)

    numbers = list(nums)

    l= len(numbers)

    sum = 0

    for i in range(l):

        sum = sum + int(numbers[i])*int(numbers[i])

    num = sum

    if sum == 1:
        print 'happy number'
        break

    print sum

