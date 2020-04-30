import tempfile
import sys
sys.setrecursionlimit(10000)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr


def two_in_one(temp1, temp2):
    len1 = 0
    len2 = 0
    with open(temp1) as temp_file1:
        for _ in temp_file1:
            len1 += 1
    temp_file1.close()

    with open(temp2) as temp_file2:
        for _ in temp_file2:
            len2 += 1
    temp_file2.close()

    i = 0
    j = 0
    with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
        with open(temp1) as temp_file1:
            with open(temp2) as temp_file2:
                line_temp1 = temp_file1.readline()
                line_temp2 = temp_file2.readline()
                while len1 > i and len2 > j:
                    if int(line_temp1) > int(line_temp2):
                        temp_file.write(line_temp2)
                        line_temp2 = temp_file2.readline()
                        j += 1
                    else:
                        temp_file.write(line_temp1)
                        line_temp1 = temp_file1.readline()
                        i += 1
                for i in range(i, len1):
                    temp_file.write(line_temp1)
                    line_temp1 = temp_file1.readline()
                for j in range(j, len2):
                    temp_file.write(line_temp2)
                    line_temp2 = temp_file2.readline()
    return temp_file


def last_result(temp):
    with open('sorted_numbers.txt', 'w') as file:
        with open(temp) as temp_file:
            for str_file in temp_file:
                file.write(str_file)


def external_sort():
    str_amount = 10000
    temp_queue = []
    work = True
    with open('numbers.txt') as file:
        while work:
            amount = 0
            arr = []
            while amount < str_amount:
                line = file.readline()
                if len(str(line)) != 0:
                    arr.append(int(line))
                    amount += 1
                else:
                    work = False
                    break
            merge_sort(arr)
            with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
                for i in arr:
                    temp_file.write(str(i)+'\n')
            temp_queue.append(temp_file.name)
    file.close()

    p = 0
    m = 1
    while m < len(temp_queue):
        file_name = two_in_one(temp_queue[p], temp_queue[m])
        temp_queue.append(file_name.name)
        p += 2
        m += 2

    last_result(temp_queue[len(temp_queue)-1])


if __name__ == '__main__':
    print("external_sort")
    external_sort()
