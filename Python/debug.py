import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# # INPUT takes path + filename (I am using a txt file)
# # RETURN returns list of tuples [(year,population),...], stick to the format of return values.
# def get_data(path, name):
#     title = "Years + 1900    Population x10^6"

#     with open(name, "w") as path:
#         path.write(title + '\n')
#     data = [(0, 1650), (10, 1750), (20, 1860), (30, 2070), (40, 2300), (50, 2560),
#             (60, 3040), (70, 3710), (80, 4450), (90, 5280), (100, 6080), (110, 6870)]
#     for items in data:
#         with open(name, "a") as path:
#             path.write(str(items[0]) + " " + str(items[1]) + '\n')
#     return data

#     # Input: a year
#     # Return: the estimate of population for that year


# def pop(year):
#     return 1436.53*(1.01395**year)

#     # # Input: data
#     # # Return: the average error as per equation 18.


# def error(data):
#     a = 0
#     for i in range(0, 12):
#         a += ((data[i][1])-pop(i*10))
#     return (1/(len(data)))*a


# data = get_data(".", "pop.txt")
# print(f"data from file:", data)
# print(f"abs(3040 - {pop(60)}) = {abs(3040 - pop(60))}")
# ave_error = round(error(data), 2)
# print(f"Average error: {ave_error}")

# # use recursion to bulid a list of even numbers


# # def even_list(n):
# #     if n == 0:
# #         return []
# #     else:
# #         return even_list(n-1) + [2*n]


# t = np.arange(0.0, 120.0)
# fig, ax = plt.subplots()

# ax.plot(t, pop(t), 'g')
# for y, p in data:
#     ax.plot(y, p, 'ro--')

# ax.set(xlabel="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
#        title="Population Model Average Error = {0}".format(ave_error))
# ax.grid()
# plt.show()


# # for i in range(0, 12):
# #     print(data[i][1])

def div_11(n):
    a = n*11
    lst = []
    b = 0
    for nums in str(a):
        lst.append(int(nums))
    # return lst
    # for i in range(1, len(lst)):
    #     b += lst[i-1]-lst[i]+lst[i+1]
    # # Returns true or false
    # if b == 0 or 11 or -11:
    #     return True
    # else:
    #     return False
    for i in range(len(lst)):
        b += lst[i]-lst[i+1]+lst[i+2]
    return b


print(div_11(319))

# for i in range(len(lst)-1, len(lst)):
#     for j in range(len(lst)+1, len(lst)):
#         for k in range(1, len(lst)):
#             print(lst[i]-lst[k]+lst[j])

# for intial in range(len(lst)):
#     first = intial
#     for i in range(first-1, len(lst)):
#         for j in range(first+1, len(lst)):
#             print(lst[i]-lst[first]+lst[j])

#   nlst = []
#    for i in lst:
#         if type(i) == int:
#             nlst.append(i)
#         else:
#             pass
#             # return False
#     return sum(nlst)


# import numpy as np


# def sl(lst, p=0):
#     # p is the depth of the list and s is the sum of the numbers at that level
#     s = []
#     a = 0
#     b = []
#     for nums in lst:
#         if type(nums) == int:
#             a += nums
#         else:
#             s.append(sl(nums, p+1))
#     if p:
#         return [p, a]
#     else:
#         return s


# prob5 = [[1, 4, [3, [100]], 3, 2, [1, [101, 1000], 5], 1, [7, 9]],
#          [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400]]],
#          [[[[100, 200, 300, 400]]], [[10, 20, 30, 40]], 1, 2, 3, 4]]
# for lst in prob5:
#     print(sl(lst))

# lst = DNA_d
# group = []
# nlst = []
# a = ""
# alst = []
# for i in range(1, len(lst)):
#     for j in range(0, len(lst[i]), 3):
#         group.append(lst[i][j:j+3])
# for cod in group:
#     for k, v in aa_d.items():
#         for values in v:
#             if cod in values:
#                 nlst.append(k[1])
#             else:
#                 nlst.append()

# for letter in nlst:
#     a += letter[0]
# return a
