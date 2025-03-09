def binarySearch(arr, l, r, x):
    # التحقق من الحالة الأساس
    if r >= l:
        mid = l + (r - l) // 2

        # إن كان العنصر المعطى موجودًا في وسط المصفوفة فسنعيد العنصر نفسه
        if arr[mid] == x:
            return mid

        # إن كان العنصر المعطى أصغر من العنصر الموجود في وسط المصفوفة
        # فإنه سيكون موجودًا في النصف الأيسر من المصفوفة قطعًا
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # وإلا فإنّ العنصر سيكون موجودًا في النصف الأيمن من المصفوفة قطعًا
        else:
            return binarySearch(arr, mid +1, r, x)

    else:
        # العنصر غير موجود في المصفوفة
        return -1


# اختبار الدالة السابقة
arr = [2, 3, 4, 10, 40,50,60,70,80]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")