def main():

    class Task:
        def __init__(self, name, duration, task_starting_hour, task_ending_hour):
            self.name = name
            self.duration = duration
            self.task_starting_hour = task_starting_hour
            self.task_ending_hour = task_ending_hour

    def get_valid_input(input_text, error_text):
        while True:
            try:
                value = int(input(input_text))
                break
            except ValueError:
                print(error_text)

        return value

    tasks = []
    end_of_tasks = 0

    print(f'\nWorking hours are from 8:00 - 16:00.')

    print(f'\nLegend: \n'
          f'1: Sunday.\n'
          f'2: Monday.\n'
          f'3: Tuesday.\n'
          f'4: Wednesday.\n'
          f'5: Thursday.')

    while end_of_tasks != -1:
        task_name = input("\nEnter task name: ")

        task_duration = get_valid_input("Enter task duration (in hours): ", "Invalid task duration")
        while not (0 < task_duration <= 8):
            task_duration = get_valid_input("Enter task duration (in hours): ", "Invalid task duration")

        task_day = get_valid_input("Enter task day (Refer to the Legend): ", "Invalid task day")
        while not (1 <= task_day <= 5):
            task_day = get_valid_input("Enter task day (Refer to the Legend): ", "Invalid task day")

        print('Please enter -1 if you don\'t want to specify starting and ending hour')

        task_starting_hour = get_valid_input("Enter task starting hour (24 hour format): ",
                                             "Invalid task starting hour")
        if task_starting_hour != -1:
            while not (8 <= task_starting_hour <= 16):
                task_starting_hour = get_valid_input("Enter task starting hour (24 hour format): ",
                                                     "Invalid task starting hour")

            task_ending_hour = get_valid_input("Enter task ending hour (24 hour format): ", "Invalid task ending hour")
            while not (8 <= task_ending_hour <= 16):
                task_ending_hour = get_valid_input("Enter task ending hour (24 hour format): ", "Invalid task ending hour")

            while task_ending_hour - task_starting_hour != task_duration:
                task_starting_hour = get_valid_input("Enter task starting hour (24 hour format): ", "Invalid task starting hour")
                task_ending_hour = get_valid_input("Enter task ending hour (24 hour format): ", "Invalid task ending hour")

        for task in tasks:
            if task.day == task_day:
                if task.task_starting_hour == task_starting_hour and task.task_ending_hour == task_ending_hour:
                    print(f'Task {task_name} is scheduled in this time range.')
                    print(f'If you would like to replace the task please reply by 1 and else reply by 0')
                    replace_task_flag = get_valid_input("Replace the task? ", "Invalid answer.")

                    while not (0 <= replace_task_flag <= 1):
                        replace_task_flag = get_valid_input("Replace the task? ", "Invalid answer.")

                    if replace_task_flag == 1:
                        task.name = task_name

            # else:
            #     if task_starting_hour == -1:
            #         for task in tasks:
            #


if __name__ == '__main__':
    main()