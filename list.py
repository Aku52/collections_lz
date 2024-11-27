from statistics import median
n = int(input("ведите количество элементов в ряду фибоначи:"))
# s - элемент последовательности, n - последний номер нужного элемента ряда
s = [0,1]
if n <= 2:
    print(f"ряд фибоначи до {n} элементов:{s[:n]}")
else:
    for i in range(2,n):
        next_number = s[-1] + s[-2]
        s.append(next_number)
    for i in range(len(s)):
        if s[i] % 2 == 0:
            s[i] *= 2
        else:
            s[i] **= 2
    print(f"ряд фибоначи до {n} эл-тов:{s}")


min_value=min(s)
max_value=max(s)
list_length=len(s)
num_elements=len(s)
med = median(s)
print("минимальный элемент",min_value)
print("максимальный элемент",max_value)
print("длина списка", list_length)
print("количество элементов",num_elements)
print("медианное значение",med)