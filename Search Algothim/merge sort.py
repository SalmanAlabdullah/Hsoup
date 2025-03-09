def merge(arr):

    if len(arr) > 1 :
        mid = len(arr) // 2
        R = arr[mid:]
        L = arr[:mid]

        merge(R)
        merge(L)

        k=j=i=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j +=1
            k +=1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1





    return arr




a = [5,4,0,2,1,9,8,3]

# طباعة المصفوفة
def printList(arr):
	for i in range(len(arr)):
		print(arr[i],end=" ")
	print()

# اختبار الدوال السابقة
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print ("Given array is", end="\n")
	printList(a)
	merge(a)
	print("Sorted array is: ", end="\n")
	printList(a)