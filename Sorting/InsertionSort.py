# def insertion_sort(A):
#     for i in range(1, len(A)):
#         for j in range(i-1, -1, -1):
#             if A[j] > A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]
#             else:
#                 break
#

def insertion_sort(A):
    for i in range(1, len(A)):
        currNum = A[i]
        j = i-1
        while j >= 0 and A[j] > currNum:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = currNum


n = int(input("Enter size of array : "))
A = []

for i in range (n):
    item = int(input("Enter item : "))
    A.append(item)

print(A,end=" ")
insertion_sort(A)
print("\nSorted list is ",A, end=" ")
