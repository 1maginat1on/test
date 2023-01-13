class Item:
    menu = {'1': 'Добавить дело', '2': 'Список дел', '3': 'Найти дело', '4': 'Найти дело по дате',
            '5': 'Удалить дело', '6': 'Список важных дел', '7': 'Выйти'}

    def __init__(self):
        self.item_items = []

    def add_item(self, items):
        self.item_items.append(items)

    def list(self):
        print('Список дел:')
        for item in self.item_items:
            print(str(item.num) + '. ' + item.item + ' (Выполнено)' * int(item.is_done))
        print()

    def find(self, find_str):
        return ((item.num, item.item) for item in self.item_items if item.item.find(find_str) != -1)

    def run(self):

        while True:
            print('Меню:')
            for num, val in Item.menu.items():
                print(num + '. ' + val, end='\n')
            command = input()
            if command == '1':
                self.add_item(ItemItem(input('Название? Дата? Оно важное?(отметьте * если да)\n')))

                print('Новое дело добавлено')
            elif command == '2':
                self.list()
            elif command == '6':
                find = self.find(input('*'))
                for num, val in find:
                    print(str(num) + '. ' + val)
            elif command == '3':
                find = self.find(input('Введите ключевое слово'))
                for num, val in find:
                    print(str(num) + '. ' + val)
            elif command == '4':
                num = int(input('Номер даты для поиска:'))
                for item in self.item_items:
                    if item.num == num:
                        item.check()
                        print(f'Вот дела на это число  {num} ')
                        break
                else:
                    print(f'Дело для {num} числа не найдено')

            elif command == '5':
                num = (input('Название дела:'))
                for item in self.item_items:
                    if item.num == num:
                        delattr(num)
                        item.uncheck()
                        print(f'Дело {num} удалено')
                        break
                else:
                    print(f'Дело {num} не найдено')

            elif command == '7':
                print('Программа завершена')
                break


class ItemItem:
    couner_do = 0

    def __init__(self, new_do):
        self.is_done = False
        ItemItem.couner_do += 1
        self.num = ItemItem.couner_do
        self.item = new_do

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False


if __name__ == '__main__':
    item_1 = Item()
    item_1.run()