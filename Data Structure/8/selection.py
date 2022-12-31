#
# select returns the k-th smallest element of a
#
def select(a, k):
  b = sorted(a)
  return b[k]

# Implement the function quick_select.
# It also returns the k-th smallest element of a.
def quick_select(a, k):
    pivot = a[0]
    small, equal, large = [], [], []
    for i in range(len(a)):
        if a[i] < pivot:
            small.append(a[i])
        elif a[i] > pivot:
            large.append(a[i])
        else:
            equal.append(a[i])
    
    if k < len(small):
        return quick_select(small, k)
    elif k < len(small) + len(equal):
        return equal[0]
    else:
        return quick_select(large, k - len(small) - len(equal))