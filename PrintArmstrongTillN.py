# # def isArmstrong(num, res=0):
# #     temp = num
# #     while temp > 0:  # Use 'temp' instead of 'num' here
# #         r = temp % 10
# #         temp = temp // 10  # Use integer division here
# #         res = res + r * r * r
# #
# #     if num == res:
# #         return True
# #     else:
# #         return False
# #
# #
# # num = int(input("Enter any number: "))
# #
# # print("Armstrong numbers till", num, "are:", end=" ")
# #
# # for i in range(2,num + 1):
# #     if isArmstrong(i):
# #         print(i, end=" ")
#
#
# def isArmstrong(num):
#     temp = num
#     num_digits = len(str(num))
#     total = 0
#
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** num_digits
#         temp //= 10
#
#     return num == total
#
# count = 0
# num = 0
#
# print("First 10 Armstrong numbers are:", end=" ")
#
# while count < 10:
#     if isArmstrong(num):
#         print(num, end=" ")
#         count += 1
#     num += 1
