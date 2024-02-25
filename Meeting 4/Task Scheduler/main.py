class Task:
    def __init__(self, name, day, duration, starting_hour, ending_hour):
        self.name = name
        self.day = day
        self.duration = duration
        self.starting_hour = starting_hour
        self.ending_hour = ending_hour


def main():
    tasks = []
    hours_list = [[None] * 8 for _ in range(5)]
    end_of_tasks = 0

    print('''
    Instructions:

    Enter -1 to end the tasks selection
    Enter -1 to refrain from picking a day
    Enter -1 to refrain from picking starting hour
    Enter -1 to refrain from picking ending hour

    Days must be between 1 and 5
    Hours must be between 8 and 16
    Duration must be synchronized with the starting and ending hours
    ''')

    while end_of_tasks != -1:
        name = input("Enter task name: ")
        day = int(input("Enter task day: "))
        duration = int(input("Enter task duration: "))
        starting_hour = int(input("Enter task starting hour: "))
        ending_hour = int(input("Enter task ending hour: "))

        # day is from 1 to 5
        # hours are from 8 to 16
        # duration is maximum 8 and minimum 0

        if day == -1:
            if starting_hour == -1:
                flag = False
                for index in hours_list:
                    for i in range(8):
                        if i + duration > len(index):
                            break
                        if index[i:i + duration] == [None] * duration:
                            index[i:i + duration] = [1] * duration
                            tasks.append(Task(name, day, duration, starting_hour, ending_hour))
                            flag = True
                            break

                    if flag:
                        break
            else:
                for index in hours_list:
                    if index[starting_hour - 8:ending_hour - 8] == [None] * duration:
                        index[starting_hour - 8:ending_hour - 8] = [1] * duration
                        tasks.append(Task(name, day, duration, starting_hour, ending_hour))
                        break

                    else:
                        print('This time range isn\'t available')

        else:
            if starting_hour == -1:
                for i in range(8):
                    if i + duration > 8:
                        break
                    if hours_list[day - 1][i:i + duration] == [None] * duration:
                        hours_list[day - 1][i:i + duration] = [1] * duration
                        tasks.append(Task(name, day, duration, starting_hour, ending_hour))
                        break
                    else:
                        print('This time range isn\'t available')
            else:
                if hours_list[day - 1][starting_hour - 8:ending_hour - 8] == [None] * duration:
                    hours_list[day - 1][starting_hour - 8:ending_hour - 8] = [1] * duration
                    tasks.append(Task(name, day, duration, starting_hour, ending_hour))
                else:
                    print('This time range isn\'t available')

        print()
        for task in tasks:
            print(f'name: {task.name}.')
        print(f'{hours_list}\n')

        end_of_tasks = int(input('End tasks? '))


if __name__ == '__main__':
    main()
