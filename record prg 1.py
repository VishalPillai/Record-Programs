def SHIFT(lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        if lst[left] >= 0:
            left += 1
        elif lst[right] < 0:
            right -= 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    print(lst)

lst=eval(input("Enter the list:"))
SHIFT(lst)
def SwapHalfList(Array):
    mid = len(Array) // 2
    if sum(Array[:mid]) > sum(Array[mid:]):
        for i in range(mid):
            Array[i], Array[mid + i] = Array[mid + i], Array[i]
    print(Array)
Array=eval(input("Enter the list:"))
SwapHalfList(Array)
def RShift(Lst):
    last = Lst[-1]
    for i in range(len(Lst) - 1, 0, -1):
        Lst[i] = Lst[i - 1]
    Lst[0] = last
    print(Lst)

lst=eval(input("Enter the list:"))
RShift(lst)
def LShift(Lst, n):
    for k in range(n):
        first = Lst[0]
        for i in range(len(Lst) - 1):
            Lst[i] = Lst[i + 1]
        Lst[-1] = first
    print(Lst)

Lst=eval(input("Enter the list:"))
n=int(input("Enter the number of Shift:"))
LShift(Lst, n)
def lst_reverse(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    print(lst)

lst=eval(input("Enter the list:"))
lst_reverse(lst)
def part_reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    print(lst)

lst=eval(input("Enter the list:"))
start=int(input("Enter the start value:"))
end=int(input("Enter the stop value:"))
part_reverse(lst, start, end)
def lst_modify():
    lst = eval(input("Enter list: "))
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                lst.pop(j)
            else:
                j += 1
        i += 1
    print(lst)
lst_modify()
def swap_loc(Array):
    for i in range(0, len(Array) - 1, 2):
        Array[i], Array[i + 1] = Array[i + 1], Array[i]
    print(Array)
Array=eval(input("Enter the list:"))
swap_loc(Array)
