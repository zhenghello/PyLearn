def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试,如果结果不是40.0，就会报错


num=[1,2,3,4,5,6,7,8,9,10]
print(average(num))

print(average([20, 30, 70]))

