"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.

Входные данные
Первая строка входного файла INPUT.TXT содержит целое число N (3 ≤ N ≤ 1000) – количество кустов черники. Вторая
строка содержит N целых положительных чисел a1, a2, ..., aN – число ягод черники, растущее на соответствующем кусте.
Все ai не превосходят 1000.

Выходные данные
В выходной файл OUTPUT.TXT выведите ответ на задачу.

[Примечание: условия задачи были даны не полностью, восстановлены из свободных источников сети Internet.]
"""

input_file = open('INPUT.txt', 'r')
bushes = int(input_file.readline())
string_of_numbers_of_berries = input_file.readline()[0::].rstrip()
input_file.close()
numbers_of_berries = string_of_numbers_of_berries.split(' ')
number_of_berries = [0] * bushes
j = 0
for i in numbers_of_berries:
    if i.isdigit():
        number_of_berries[j] = int(i)
        j += 1
j = 0
max_result = 0
current_sum = 0
for i in range(len(number_of_berries)):
    if i == 0:
        current_sum = number_of_berries[i] + number_of_berries[i+1] + number_of_berries[len(number_of_berries)-1]
    elif i == len(number_of_berries)-1:
        current_sum = number_of_berries[i] + number_of_berries[i - 1] + number_of_berries[0]
    else:
        current_sum = number_of_berries[i] + number_of_berries[i + 1] + number_of_berries[i - 1]
    if current_sum > max_result:
        max_result = current_sum
print(f'You can get {max_result} berries at once.')
output_file = open('OUTPUT.txt', 'w')
output_file.write(f'You can get next number of berries at once according to data from INPUT.txt:\n{max_result}')
output_file.close()
