def sqrt(x):
    if x < 0:  # الجذر التربيعي غير معرف للأعداد السالبة
        return None

    # حدود البحث
    left, right = 0, x

    # الدقة المطلوبة
    epsilon = 0.0001

    while right - left > epsilon:
        mid = (left + right) / 2

        if mid * mid < x:
            left = mid
        elif mid * mid > x:
            right = mid
        else:
            return mid  # إذا كان الجذر مضبوطًا تمامًا

    return (left + right) / 2  # تقريب الجذر

# اختبار الكود
print(sqrt(16))   # النتيجة: 4
print(sqrt(20))   # النتيجة: 4.4721 تقريبًا
