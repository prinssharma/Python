def selection_sort(A):
    for i in range(0,len(A)-1):
        min_index = i
        for j in range(i+1,len(A)):
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[i],A[min_index] = A[min_index], A[i]


n = int(input("Enter size of array : "))
A = []

for i in range (n):
    item = int(input("Enter item : "))
    A.append(item)

print(A,end=" ")
selection_sort(A)
print("\nSorted list is ",A, end=" ")