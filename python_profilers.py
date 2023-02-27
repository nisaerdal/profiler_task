import random
import cProfile

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

if _name_ == "_main_":
    # Rastgele sayılardan oluşan bir liste
    lst = [random.randint(0, 1000) for i in range(10000)]
    # performans analizi için cProfile
    print("Bubble Sort ve Selected Sort")
    cProfile.run("bubble_sort(lst)")
    cProfile.run("selection_sort(lst)")