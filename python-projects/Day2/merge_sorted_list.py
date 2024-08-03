# Write a Python script to merge two sorted lists into one sorted list

def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merge_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1

        else:
            merge_list.append(list2[j])
            j += 1

    while i < len(list1):
        merge_list.append(list1[i])
        i += 1

    while j < len(list2):
        merge_list.append(list2[j])
        j += 1

    return merge_list


# Test the function
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))
