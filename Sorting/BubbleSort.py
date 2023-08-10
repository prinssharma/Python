def bubble_sort(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A [j+1]:
                A[j], A[j+1] = A[j+1], A[j]



n = int(input("Enter size of array : "))
A = []

for i in range (n):
    item = int(input("Enter item : "))
    A.append(item)

print(A,end=" ")
bubble_sort(A)
print("\nSorted list is ",A, end=" ")