# let assume we need to add 5 in every element in the list
l = [2, 3, 4, 5, 6, 7]

# normal approach
l1 = []
for i in l:
    l1.append(i + 5)
print(l1)


# "Map" way to do it
def addi(a):
    return a + 5


print(list(map(addi, l)))
print(list(map(lambda a: a + 5, l)))

# Filter -- extract the no which is even

"""filter function which used to work"""


def even(a):
    if a % 2 == 0:
        return a


print(list(filter(even, l)))

# 'REDUCE' function use to whole summation or multiplication or many other work relate to every pair of element one br one

from functools import reduce


def mull(a, b):
    return a * b


print(reduce(mull,l))

# understanding
"""l=[1,2,3,4,5]
what it do in steps
 1st--mull(1,2)
 2nd--put output in mull(<output>,3)
 go on ... till end"""
