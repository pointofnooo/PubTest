# 1. Ввод последовательности и преобразование её в список
def StartSequence():
    while True:
        try:
            sequence = [int(x) for x in input("Введите последовательность чисел через пробел").split()]
            return sequence
        except ValueError:
            print("Введите целое число. Повторите ввод")

sequence = StartSequence()

# 2. Сортировка введённых чисел по возрастанию
for i in range(len(sequence)):
    idx_min = i
    for j in range(i, len(sequence)):
        if sequence[j] < sequence[idx_min]:
            idx_min = j
    if i != idx_min:
        sequence[i], sequence[idx_min] = sequence[idx_min], sequence[i]
# ввод искомого значения
while True:
    try:
        element = int(input("Введите любое положительное значение из списка:"))
        if element < min(sequence) or element > max(sequence):
            print("Указанное значение не входит в диапазон")
        if element <= 0:
            raise Exception
        break
    except ValueError:
        print("Введите целое число")
    except Exception:
        print("Введите положительное значение из списка")
# 3. Бинарный поиск по введённому значению
def binary_search(sequence, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sequence[middle] == element:
        return middle
    elif element < sequence[middle]:
        return binary_search(sequence, element, left, middle - 1)
    else:
        return binary_search(sequence, element, middle + 1, right)

print("Порядковый номер числа в списке:", binary_search(sequence, element, 0, len(sequence) - 1))
