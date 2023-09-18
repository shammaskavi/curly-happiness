import random
# All hail Randomness 

def mergeSort(list):
    """Sorts a list in ascending order using a merge sort algo 💅"""
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]
        mergeSort(right_half)
        mergeSort(left_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
                # i = i + 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

            while i < len(left_half):
                list[k] = left_half[i]
                i += 1
                k += 1
            print(list)
            while j < len(right_half):
                list[k] = right_half[j]
                j += 1
                k += 1
            print(list)
    return list


user_list = []
for i in range(10):
    user_list.append(random.randint(0, 90))

print(f"unsorted list: {user_list}")
print(f"sorted list: {mergeSort(user_list)}")
