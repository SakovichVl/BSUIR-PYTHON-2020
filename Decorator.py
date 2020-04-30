result = {}


def sum_result(foo):
    return foo + 5


def cached(func):
    def res_check(*args, **kwargs):
        res = result.get(args + tuple(kwargs.items()), "no")
        if res == "no":
            res = func(*args + tuple(kwargs.items()))
            result.update({args + tuple(kwargs.items()): res})
        return res

    return res_check


decorator = cached(sum_result)
