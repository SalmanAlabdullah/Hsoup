def diff(x,mid):
    if x < (mid*mid*mid):
        return (mid*mid*mid)-x
    else:
        return x - (mid*mid*mid)

def sqr(x):
    start = 0
    end = x



    while True:
        mid = (end + start) / 2
        error = diff(x,mid)


        if error <= 0.0001:
            return mid

        if (mid*mid*mid) < x :
            start = mid


        if (mid*mid*mid)>x:
            end = mid



print(sqr(16))
