from tkinter.messagebox import NO
from wsgiref.util import guess_scheme


def binary_search(item,list):
    low =0
    high = len(list)-1
    
    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        
        if guess==item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


