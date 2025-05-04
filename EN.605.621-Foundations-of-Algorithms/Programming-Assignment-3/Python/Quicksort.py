import Partition

def TextbookMethod(A, p, r):
    """
    Textbook version of quicksort algorithm. \n
    This is found on page 183 of the textbook
    """
    KeyPoints = 0

    if p < r:
        q, KeyPoints = Partition.TextbookMethod(A, p, r)
        KeyPoints += TextbookMethod(A, p, q - 1)
        KeyPoints += TextbookMethod(A, q + 1, r)

    return KeyPoints

def MedianOfThreeMethod(A, p, r):
    """
    Median-of-three version of quicksort algorithm.
    """
    KeyPoints = 0

    if p < r:
        q, KeyPoints = Partition.MedianOfThreeMethod(A, p, r)
        KeyPoints += MedianOfThreeMethod(A, p, q - 1)
        KeyPoints += MedianOfThreeMethod(A, q + 1, r)

    return KeyPoints