def bubbleSort(arr):
    n = len(arr)

    # التنقل عبر جميع عناصر المصفوفة
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            # التنقل عبر عناصر المصفوفة بدءًا من 0
            # n-i-1 وانتهاءً بالقيمة
            # نجري عملية التبديل إن كان العنصر الذي عثرنا عليه
            # أكبر من العنصر اللاحق
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # إن لم تُجر عملية التبديل في الحلقة التكرارية الداخلية
        # تتوقف الدالة عن العمل
        if swapped == False:
            break


# اختبار الدالة السابقة
arr = [64, 34, 25, 12, 22, 11, 90]
for i in range(100):
    arr.append(arr[i])

print(arr)

bubbleSort(arr)

print("Sorted array :")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

print(arr)