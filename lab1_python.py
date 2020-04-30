import operator
import argparse
import random


def sentence_maker (string, amount):
    string_list = list(string.keys())
    string_list = reversed (string_list)
    string_list = list(string_list)
    sentence = ""
    for word in range(amount):
            sentence += string_list[word] + " "
    return sentence


def quick_sort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quick_sort(s_nums) + e_nums + quick_sort(m_nums)


def str_to_arr(numbers):
    numbers = [int(i) for i in numbers.split(" ")]
    return numbers


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


def repeat_words(string):
   amount_dict = dict()
   stringWorker = string.split()
   for word in stringWorker:
        if word in amount_dict:
            amount_dict[word] +=1
        else:
            amount_dict[word] = 1
   return amount_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', type=int, metavar='', required=True, help='number of task')
    parser.add_argument('-a', '--amount', type=int, metavar='', required=True)
    args = parser.parse_args()

    with open('pytext.txt') as fileOpen:
        dataFile = fileOpen.readlines()
    numbers = str_to_arr(dataFile[1])
    if args.task == 1:
        print(repeat_words(dataFile[0]))
    elif args.task == 2:
        print(sentence_maker(repeat_words(dataFile[0]), args.amount))
    elif args.task == 3:
        print(quick_sort(numbers))
    elif args.task == 4:
        print(merge_sort(numbers))
    elif args.task == 5:
        fib = fibonacci(args.amount)
        print([num for num in fib])
