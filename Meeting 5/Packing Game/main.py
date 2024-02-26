class Item:
    def __init__(self, weight):
        self.weight = weight


class ColoredItem(Item):
    def __init__(self, weight, color):
        super().__init__(weight)
        self.color = color


class UniversalCharger(ColoredItem):
    def __init__(self, color, price, size, brand, weight):
        super().__init__(weight, color)
        self.price = price
        self.size = size
        self.brand = brand


class Passport(ColoredItem):
    def __init__(self, color, weight, cost, bought_from):
        super().__init__(weight, color)
        self.cost = cost
        self.bought_from = bought_from


class SunGlasses(ColoredItem):
    def __init__(self, have_case, color, origin, weight):
        super().__init__(weight, color)
        self.have_case = have_case
        self.origin = origin


class Sneakers(Item):
    def __init__(self, brand, new, bought_from, weight):
        super().__init__(weight)
        self.brand = brand
        self.new = new
        self.bought_from = bought_from


class ElectronicItem(Item):
    def __init__(self, weight, brand):
        super().__init__(weight)
        self.brand = brand


class SmartPhone(ElectronicItem):
    def __init__(self, brand, operating_system, storage, display, camera, materials, weight):
        super().__init__(weight, brand)
        self.operating_system = operating_system
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials


class Laptop(ElectronicItem):
    def __init__(self, brand, processor, ram, storage, graphics, weight):
        super().__init__(weight, brand)
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.graphics = graphics


class SmartWatch(ElectronicItem):
    def __init__(self, brand, display, battery_life, fitness_features, connectivity, weight):
        super().__init__(weight, brand)
        self.display = display
        self.battery_life = battery_life
        self.fitness_features = fitness_features
        self.connectivity = connectivity


class Campus(ElectronicItem):
    def __init__(self, brand, accuracy, price, materials, weight):
        super().__init__(weight, brand)
        self.accuracy = accuracy
        self.price = price
        self.materials = materials


class Bag:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def add_item_limited(self, new_item):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight

        if new_item.weight + total_weight > 80:
            print(f'You have exceeded the allowed weight: {new_item.weight + total_weight}\n')
        elif len(self.items) == 6:
            print(f'You have exceeded the allowed quantity: 7\n')
        else:
            self.items.append(new_item)
            print(f'The item was added successfully\n')

    def remove_item(self, index):
        self.items.remove(self.items[index - 1])
        print(f'The item was removed successfully\n')

    def print_all_items(self):
        for i, item in enumerate(self.items):
            print(f'{i + 1} - {item.__class__.__name__} {item.__dict__}')

    def print_by_category(self):
        print('\nColored Items')
        for i, item in enumerate(self.items):
            if isinstance(item, ColoredItem):
                print(f'{i + 1} - {item.__class__.__name__} {item.__dict__}')

        print('\nSneakers')
        for i, item in enumerate(self.items):
            if isinstance(item, Sneakers):
                print(f'{i + 1} - {item.__class__.__name__} {item.__dict__}')

        print('\nElectronic Items')
        for i, item in enumerate(self.items):
            if isinstance(item, ElectronicItem):
                print(f'{i + 1} - {item.__class__.__name__} {item.__dict__}')

    def print_one_category(self, category, item_type):
        print(f'\n{item_type}')
        for i, item in enumerate(self.items):
            if isinstance(item, category):
                print(f'{i + 1} - {item.__class__.__name__} {item.__dict__}')


def main():
    items = Bag()
    items.add_item(UniversalCharger('Black', 50, 'Medium', 'Lenovo', 12))
    items.add_item(Passport('Blue', 1, 50, 'USA'))
    items.add_item(SunGlasses(True, 'Black', 'Italy', 10))
    items.add_item(Sneakers('New Balance', False, 'Spain', 14))
    items.add_item(SmartPhone('Apple', 'IOS', 128, 'AMOLED', 'Dual Lens', ['Lithium', 'Plastic'], 50))
    items.add_item(Laptop('Dell', 'Intel i7', 16, 512, 'NVIDIA GetForce 4', 60))
    items.add_item(SmartWatch('Samsung', 'Touchscreen', 3, 'Heart Rate Monitor', 'Bluetooth', 44))
    items.add_item(Campus('Samsung', 'high', 50, ['Iron', 'Plastic'], 4))

    items.print_all_items()

    bag = Bag()

    print(f'\nLegend:\n\t1: Add Item\n\t2: Remove Item\n\t10: Print Bag\n\t-1: Finish\n')
    while True:
        while True:
            try:
                add_remove = int(input('Please choose what you want to do. Refer to the Legend above: '))
                if add_remove != 1 and add_remove != 0 and add_remove != -1 and add_remove != 10:
                    raise ValueError
                break
            except ValueError:
                print('Invalid input')

        if add_remove == -1:
            break

        if add_remove == 10:
            bag.print_all_items()
            print()

        elif add_remove == 1:
            while True:
                try:
                    add_item_choice = int(input('Enter the item you want to add to the bag (1 to 8): '))
                    if not (1 <= add_item_choice <= 8):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid item')

            bag.add_item_limited(items.items[add_item_choice - 1])

        elif len(bag.items) == 0:
            print(f'You have {len(bag.items)} items and there is nothing to remove\n')

        else:
            while True:
                try:
                    remove_item_choice = int(input(f'Enter the item you want to remove from the bag (1 to {len(bag.items)}): '))
                    if not (1 <= remove_item_choice <= len(bag.items)):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid item')

            bag.remove_item(remove_item_choice)

    bag.print_by_category()

    print(f'\nLegend:\n\t1: Colored Items\n\t2: Sneakers\n\t3: Electronic Items\n\t-1: Finish\n')
    while True:
        while True:
            try:
                category = int(input('Please choose a category. Refer to the Legend above: '))
                if category != 1 and category != 2 and category != 3 and category != -1:
                    raise ValueError
                break
            except ValueError:
                print('Invalid Category')

        if category == -1:
            break
        elif category == 1:
            bag.print_one_category(ColoredItem, 'Colored Items')
        elif category == 2:
            bag.print_one_category(Sneakers, 'Sneakers')
        elif category == 3:
            bag.print_one_category(ElectronicItem, 'Electronic Items')

        print()


if __name__ == '__main__':
    main()
