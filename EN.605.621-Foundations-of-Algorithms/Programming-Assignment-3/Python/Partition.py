import math as Math

def _Partition(A, p, r):
    """
    Internal function handling the core functionality of partition logic. \n
    This is found on page 184 of the textbook
    """
    KeyPoints = 0

    x = A[r]
    i = p - 1

    for j in range(p, r):

        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

        KeyPoints += 1
        
    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1, KeyPoints

def TextbookMethod(A, p, r):
    """
    Textbook version of partition logic.
    """
    
    return _Partition(A, p, r)     

def MedianOfThreeMethod(A, p, r):
    """
    Median-of-three version of partition logic. \n
    Additional logic to calculate and use median-of-three index before calling _Partition.
    """
    
    MedianOfThreeIndex = CalculateMedianOfThreeIndex(A, p, r)
    A[r], A[MedianOfThreeIndex] = A[MedianOfThreeIndex], A[r]

    return _Partition(A, p, r)

def CalculateMedianOfThreeIndex(A, i, j):
    """
    Helper function for determining median-of-three index.
    """

    k = Math.floor((i + j) / 2)

    if ((A[i] > A[k]) ^ (A[i] > A[j])):
        # A[i] is median value
        return i
    elif((A[k] > A[i]) ^ (A[k] > A[j])):
        # A[k] is median value
        return k
    else:
        # A[j] is median value
        return j