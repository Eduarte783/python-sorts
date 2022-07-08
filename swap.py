
li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

def bubble_sort(li):
    for num in range(len(li) - 1, 0, -1):
        for i in range(num):
#    for i in range(len(li) - 1):
            if li[i] > li[i+1]:
 #               (li[i], li[i+1]) = (li[i+1], li[i])
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp

    return True

bubble_sort(li)
print(li)