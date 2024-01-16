# def add(*args):
#     sum_num = 0
#     for i in args:
#         sum_num += i
#     return sum_num
#
#
# sum_list = add(2, 3, 4, 5)
# print(sum_list)


def calc(n, **kwargs):
    n += kwargs.get('add')
    n *= kwargs.get('multy')
    return n


dupa = calc(2, add=7, multy=5)

print(dupa)


class Car:

    def __init__(self, **kw):
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(model="Toyota", color='blue')
print(my_car.model, my_car.color, my_car.seats)
