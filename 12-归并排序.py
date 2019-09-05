num = [10, 1, 35, 61, 89, 36, 55]


def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])

    return merge(left, right)


def merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    print(merge_sort(num))

