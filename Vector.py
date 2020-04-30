class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class Vector(object):

    def __init__(self, obj):
            self.vector = obj

    def __add__(self, second_vector):
       try:
        if len(self.vector) != len(second_vector):
            raise MyError("first vector!= second vector")
        for i in range(len(self.vector)):
            self.vector[i] += second_vector.vector[i]
        return self.vector 
       except MyError as mr:
            print(mr)
        

    def __sub__(self, second_vector):
        if len(self.vector) != len(second_vector):
            raise MyError("first vector!= second vector")
        for i in range(len(self.vector)):
            self.vector[i] -= second_vector.vector[i]
        return self.vector

    def __str__(self):
        string = ""
        for elem in self.vector:
            string += str(elem) + ','
        return string[:len(string)-1]

    def __mul__(self, second_vector):
        if len(self.vector) != len(second_vector):
            raise MyError("first vector!= second vector")
        mul = 0
        for i in range(len(self.vector)):
            mul += self.vector[i] * second_vector.vector[i]
        return mul

    def __const_mul__(self, const):
        self.vector = list(a * const for a in self.vector)
        return self.vector

    def __len__(self):
        return len(self.vector)

    def __index__(self, index):
        arr = list(self.vector)
        return arr[index]
