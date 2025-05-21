nums = range(1, 11)
chet = [num for num in nums if num % 2 == 0]
nechet = [num for num in nums if num % 2 != 0]
sum_chet = sum(chet)
sum_nechet = sum(nechet)


students = {}
students['Bob'] = 5
students['Alice'] = 4
students['Charlie'] = 3
students['David'] = 5
sr_ocenka = sum(students.values()) / len(students.values())
print(sr_ocenka)


def obrat_str(s):
    return s[::-1]

print(obrat_str('vovka'))
nums = [1, 2, 3, 4, 5]
del_nums = []
while nums:
    num = nums.pop()
    print(f'Число {num} удалено из списка.')
    del_nums.append(num)
del_nums.sort()
print(del_nums)


pets = ['cat', 'dog', 'fish', 'cat', 'dog', 'cat', 'frog']

while 'cat' and 'dog' in pets:
    pets.remove('cat')
    pets.remove('dog')
print(pets)
pe
