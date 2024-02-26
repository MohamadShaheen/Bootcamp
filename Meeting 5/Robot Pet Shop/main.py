from faker import Faker
import random


class Robot:
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type):
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.name = name
        self.robot_id = robot_id
        self.battery_type = battery_type
        self.animal_type = animal_type


class RobotForSale(Robot):
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type):
        super().__init__(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type)


class RobotBroken(Robot):
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type):
        super().__init__(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type)


class RobotInRepair(Robot):
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type):
        super().__init__(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type)


class RobotReadyToBeShipped(Robot):
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type):
        super().__init__(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type)


class RobotSold(Robot):
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type):
        super().__init__(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type)


class RobotEmployee(Robot):
    def __init__(self, name, robot_id, battery_type, daily_salary):
        super().__init__('Employee Material', -1, -1, name, robot_id, battery_type, 'Employee')
        self.daily_salary = daily_salary


class Store:
    def __init__(self):
        self.employees = []
        self.robots = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_robot(self, robot):
        self.robots.append(robot)

    def print_all_robots(self):
        for i, employee in enumerate(self.employees):
            print(f'{i + 1} - {employee.__class__.__name__} - {employee.__dict__}')

        print()

        for i, robot in enumerate(self.robots):
            print(f'{i + 1} - {robot.__class__.__name__} - {robot.__dict__}')

    def print_robots_for_sale(self):
        print('Robots For Sale')
        for i, robot in enumerate(self.robots):
            if isinstance(robot, RobotForSale):
                print(f'{i + 1} - {robot.__class__.__name__} - {robot.__dict__}')

    def print_robots_for_sale_price_range(self, minimum_price, maximum_price):
        print(f'Robots For Sale For {minimum_price}$ - {maximum_price}$')
        for i, robot in enumerate(self.robots):
            if isinstance(robot, RobotForSale):
                if minimum_price <= robot.price <= maximum_price:
                    print(f'{i + 1} - {robot.__class__.__name__} - {robot.__dict__}')

    def print_employees_salary_cost(self):
        print('Employees Salary Cost')
        total_cost = 0
        for i, employee in enumerate(self.employees):
            print(f'{i + 1} - {employee.daily_salary}$')
            total_cost += employee.daily_salary

        print(f'Employees Total Daily Salary Cost - {total_cost}$')

    def print_total_store_balance(self):
        total_store_balance = 0

        for i, robot in enumerate(self.robots):
            if isinstance(robot, RobotForSale) or isinstance(robot, RobotSold) or isinstance(robot, RobotReadyToBeShipped):
                total_store_balance += robot.price
            elif isinstance(robot, RobotBroken) or isinstance(robot, RobotInRepair):
                total_store_balance -= robot.cost_to_fix_per_day

        for i, employee in enumerate(self.employees):
            total_store_balance -= employee.daily_salary

        print(f'Total Store Balance - {total_store_balance}$')

    def print_robot_details(self, robot_id):
        print(f'Robot {robot_id} Details')

        for employee in self.employees:
            if employee.robot_id == robot_id:
                print(f'{employee.__class__.__name__} - {employee.__dict__}')

        for robot in self.robots:
            if robot.robot_id == robot_id:
                print(f'{robot.__class__.__name__} - {robot.__dict__}')


def main():
    fake = Faker('en_US')
    store = Store()

    def generate_random_details():
        main_material = random.choice(['Bronze', 'Iron', 'Steel', 'Mithril', 'Adamant', 'Rune'])
        price = random.randint(100, 1000)
        cost_to_fix_per_day = random.randint(1, 20)
        name = fake.name()
        robot_id = fake.random_number(digits=9)
        battery_type = random.choice(['Lithium', 'Alkaline'])
        animal_type = random.choice(['Herbivore', 'Carnivore'])

        return main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type

    for _ in range(3):
        _, _, _, name, robot_id, battery_type, _ = generate_random_details()
        daily_salary = random.randint(30, 50)

        store.add_employee(RobotEmployee(name, robot_id, battery_type, daily_salary))

    for _ in range(100):
        main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type = generate_random_details()
        robot_type = random.randint(1, 5)

        id_to_print = robot_id

        if robot_type == 1:
            store.add_robot(RobotForSale(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type))
        elif robot_type == 2:
            store.add_robot(RobotBroken(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type))
        elif robot_type == 3:
            store.add_robot(RobotInRepair(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type))
        elif robot_type == 4:
            store.add_robot(RobotReadyToBeShipped(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type))
        else:
            store.add_robot(RobotSold(main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type))

    store.print_all_robots()
    print()
    store.print_robots_for_sale()
    print()
    store.print_robots_for_sale_price_range(100, 300)
    print()
    store.print_employees_salary_cost()
    print()
    store.print_total_store_balance()
    print()
    store.print_robot_details(id_to_print)


if __name__ == '__main__':
    main()
