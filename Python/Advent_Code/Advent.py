

# def sumLst(dict):
#     lst = []
#     for k, v in dict.items():
#         lst += k, sum(v)
#     return lst


# dict = {"elf1": [1000, 2000, 3000],
#         "elf2": [4000],
#         "elf3": [5000, 6000],
#         "elf4": [7000, 8000, 9000],
#         "elf5": [10000]
#         }
# print(sumLst(dict))

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().splitlines()

calories_per_elf: list[int] = []
current_calories = 0

for value in data:
    if value:
        current_calories += int(value)
    else:
        calories_per_elf.append(current_calories)
        current_calories = 0


# part 1
print(max(calories_per_elf))

# part 2
calories_per_elf.sort(reverse=True)
print(sum(calories_per_elf[:3]))
