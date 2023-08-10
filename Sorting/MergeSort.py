def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)

def merge_sort2(A, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort2(A, first, mid)
        merge_sort2(A, mid + 1, last)
        merge(A, first, mid, last)

def merge(A, first, mid, last):
    L = A[first:mid + 1]
    R = A[mid + 1:last + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0
    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

n = int(input("Enter size of array: "))
A = []

for i in range(n):
    item = int(input("Enter item: "))
    A.append(item)

print("Unsorted list:", A)
merge_sort(A)
print("Sorted list:", A)
