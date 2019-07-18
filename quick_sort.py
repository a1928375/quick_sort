import random
def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop()  
        less, greater = [], []
        for val in A:
            if val < pivot:
                less.append(val)
            else:
                greater.append(val)
        return quick_sort(less) + [pivot] + quick_sort(greater)


A = [3, 4, 2, 5, 3, 8, 1]
print(quick_sort(A))
