import unittest
import ToJson
import Merge_sort
import Decorator
import Vector
import random
import json


test_vector1 = Vector.Vector([0])  
test_vector2 = Vector.Vector([0, 0, 0])
test_vector3 = Vector.Vector([6, 5, 4])
test_vector4 = Vector.Vector([1, 1, 1])
test_int = 9812398123
test_float = 2183.1
test_string = "oi mama mama ment na menya gazyet"
test_list = ["palochkoi", 3 + 9j, "chtoto", 'koldyet']
test_dict = {'kupit': ['by dzip', None, "bronirovannyi"], "ves' zaryazhennyi": 15, '5': 'tonirovannyi'}
test_tuple = (1, 'foo', "tbol'chik")
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
Dict2 = {'Hm': 'Kl'}
Dict3 = {1: [1.2, 2.2, 3.3, 4.4]}
this_list = ["apple", "banana", "cherry"]
Dict4 = {'list': this_list}
this_list2 = [False, True, None]
Dict5 = {'Dict': this_list2}
in_dict = {'Name': 'Geeks'}
Dict6 = {'Dict': in_dict}

class UnitTest(unittest.TestCase):

    def test_converter(self):
        self.assertEqual(ToJson.dict_transform(Dict), json.dumps(Dict))
        self.assertEqual(ToJson.dict_transform(Dict2), json.dumps(Dict2))
        self.assertEqual(ToJson.dict_transform(Dict5), json.dumps(Dict5))
        self.assertEqual(ToJson.dict_transform(Dict6), json.dumps(Dict6))
        self.assertEqual(ToJson.to_json(Dict3), json.dumps(Dict3))
        self.assertEqual(ToJson.to_json(Dict4), json.dumps(Dict4))

    def test_merge(self):
        with open('numbers.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-100000, 100000)) for _ in range(100005))
        Merge_sort.external_sort()
        check = True
        with open('sorted_numbers.txt', 'r') as file:
            for line in file:
                temp = int(line)
                if int(line) >= temp:
                    temp = int(line)
                else:
                    check = False
                    break
        self.assertEqual(check, True)

    def test_decorator(self):
        self.assertEqual(Decorator.decorator(3), 8)
        self.assertEqual(Decorator.decorator(8), 13)
        self.assertEqual(Decorator.decorator(3), 8)
        self.assertEqual(Decorator.decorator(0), 5)

    def test_vector(self):
        self.assertEqual(test_vector3.__add__(test_vector4), [7, 6, 5])
        self.assertEqual(test_vector3.__sub__(test_vector2), [7, 6, 5])
        self.assertEqual(test_vector4.__sub__(test_vector3), [-6, -5, -4])
        self.assertEqual(test_vector3.__str__(), "7,6,5")
        self.assertEqual(test_vector4.__mul__(test_vector4), 77)
        self.assertEqual(test_vector3.__const_mul__(3), [21, 18, 15])
        self.assertEqual(test_vector3.__len__(), 3)
        self.assertEqual(test_vector1.__add__(test_vector4), None);
        self.assertEqual(test_vector3.__index__(1), 18)


if __name__ == '__main__':
    unittest.main()
