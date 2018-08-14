def qiuck_sort(array):
    if len(array) < 2:
        return array;
    else:
        pivotal = array[0]
        less = [i for i in array[1:] if i <= pivotal]
        greater = [i for i in array[1:] if i > pivotal]
        return qiuck_sort(less) + [pivotal] + qiuck_sort(greater)

print(qiuck_sort([4,12,54,65,34,23,12,43]))
