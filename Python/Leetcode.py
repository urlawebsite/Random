class problem:
    def __init__(self, l1, l2):
        self.a = l1
        self.b = l2

    def get_num1(self):
        return self.a

    def get_num2(self):
        return self.b

    def add(self):
        pass

    # def add(l1, l2):
    #     a = ''
    #     b = ''
    #     # lst = []
    #     # # lst2 = []
    #     # for i in range(len(l1)):
    #     #     a += str(l1[i])
    #     #     b += str(l2[i])
    #     for nums in l1:
    #         a += str(nums)
    #     for nums2 in l2:
    #         b += str(nums2)
    #     num = int(a[::-1])
    #     num2 = int(b[::-1])
    #     sum = num + num2
    #     return sum


l1 = [2, 4, 3]
l2 = [5, 6, 4]

print(l1, l2)
# print(342+465)
# print(add(l1, l2))
x = problem(l1, l2)
print(x)
