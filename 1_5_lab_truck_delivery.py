"""
Доставка вантажів. Користувачам надається можливість
оформлення замовлень на доставку товарів, відстеження поточного
стану замовлення. Оператори можуть змінювати стан замовлення. Для
кожного замовлення обирається відповідний автомобіль для доставки.
"""
import itertools


orders = {}


def create_new_order():
    order = Order()
    order.status = ORDER_STATUS['1']
    order.car = input('Укажите автомобиль: ') or 'Tesla Semi'
    orders[order.id] = order


def check_order():
    try:
        order_id = input('Укажите ИД заказа: ')
        order = orders[order_id]
        print(order)
    except Exception as e:
        print('Что-то пошло не так...')


def change_order_status():
    try:
        order_id = input('Укажите ИД заказа: ')
        order = orders[order_id]
        print(ORDER_STATUS)
        status = input('Укажите новый статус: ')
        order.status = ORDER_STATUS[status]
        print('Статус изменен')
    except Exception as e:
        print('Что-то пошло не так...')


def print_all_orders():
    print(orders)


MENU_ACTION = {
    '1': create_new_order,
    '2': check_order,
    '3': change_order_status,
    '4': print_all_orders,
    '5': exit
}


ORDER_STATUS = {
    '1': 'В работе',
    '2': 'Завершен',
    '3': 'Отменен'
}


class Order(object):
    new_id = itertools.count()

    def __init__(self):
        self.id = str(next(self.new_id))
        self.status = None
        self.car = None

    def __str__(self):
        return 'Ид: {}, Статус: {}, Автомобиль: {}'.format(self.id, self.status, self.car)

    def __repr__(self):
        return 'Данные о заказе: (Ид: {}, Статус: {}, Автомобиль: {})'.format(self.id, self.status, self.car)


def print_main_menu():
    print('> 1. Новый заказ')
    print('> 2. Проверить заказ')
    print('> 3. Изменить заказ')
    print('> 4. Показать все заказы')
    print('> 5. Выход')


def main():
    while True:
        print_main_menu()
        action = input('Ваш выбор: ') or 0
        try:
            func = MENU_ACTION[action]
            func()
        except Exception as e:
            print('***Неправильный ввод***')


if __name__ == "__main__":
    main()
