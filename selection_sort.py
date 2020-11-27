def selection_sort(li):
    for i in range(len(li)):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]

    print(li)


b = [8, 0, 2, 5, 3, 7, 4]
selection_sort(b)