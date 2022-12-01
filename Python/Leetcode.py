def add(l1, l2):
    a = ''
    b = ''
    # lst = []
    # # lst2 = []
    # for i in range(len(l1)):
    #     a += str(l1[i])
    #     b += str(l2[i])
    for nums in l1:
        a += str(nums)
    for nums2 in l2:
        b += str(nums2)
        num = int(a[::-1])
        num2 = int(b[::-1])
        sum = num + num2
    return sum


# l1 = [2, 4, 3]
# l2 = [5, 6, 4]

# print(l1, l2)
# # print(342+465)
# print(add(l1, l2))

# still working on it

# def twoSum(n, t):
#     for num in n:
#         for nums in t:
#             for pos in num:
#                 if num + nums == t:
#                     return t
#                 else:
#                     return "target not met"


# n = [2, 7, 11, 15]
# t = 9
# print("Input:" + " " + str(n))
# print("Output: [0,1]")
# print(twoSum(n, t))
