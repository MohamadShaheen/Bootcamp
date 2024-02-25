from datetime import datetime


# Create loggers
def create_logger(log_type='message'):
    # Logging with message
    def logger(message):
        print(message)

    # Logging with message + timestamp
    if log_type == 'timestamp':
        def logger(message):
            print(f'{datetime.now()}: {message}')

    # Logging with message + timestamp + level
    elif log_type == 'level':
        def logger(message):
            def log_with_level(level):
                print(f'{datetime.now()} ({level.upper()}): {message}')
            return log_with_level

    # Logging with event + date
    elif log_type == 'event_date':
        def logger():
            def log_with_event_date(event, date):
                print(f'{event} occurred at {date}')
            return log_with_event_date

    return logger


# Log processing function
def create_log_filter(criteria='date'):
    def filter_logs(logs):
        # Filter out no date / timestamp logs
        if criteria == 'date':
            return [log for log in logs if '2023' in log]

        # Filter logs in given timestamp
        elif criteria == 'timestamp_range':
            start = datetime(2024, 1, 1)
            end = datetime(2024, 12, 31)
            return [log for log in logs if start <= datetime.strptime(log[:10], '%Y-%m-%d') <= end]

        # Filter logs by message length
        elif criteria == 'message_length':
            return [log for log in logs if len(log) <= 20]

    return filter_logs


def main():
    logger = create_logger('message')
    logger('Hey. I am Mohamad.')

    timestamp_logger = create_logger('timestamp')
    timestamp_logger('Hey. I am Mohamad.')

    level_logger = create_logger('level')
    warn_logger = level_logger('Warning. I am Mohamad.')
    warn_logger('warn')

    event_date_logger = create_logger('event_date')
    dance_logger = event_date_logger()
    dance_logger('Dance', datetime.now())

    print('\n# -------------------------------------------------------------------------------------\n')

    logs = [
        '2024-02-25: new log',
        '2023-01-01: old log.',
        '2024-03-01: a damn long log'
    ]

    filter_by_date = create_log_filter('date')
    print(f'Date Filter: {filter_by_date(logs)}')

    filter_by_timestamp = create_log_filter('timestamp_range')
    print(f'Timestamp Fitler: {filter_by_timestamp(logs)}')

    filter_by_length = create_log_filter('message_length')
    print(f'Length Filter: {filter_by_length(logs)}')


if __name__ == '__main__':
    main()
