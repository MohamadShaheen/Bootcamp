import random
import time

from faker import Faker
from social_media.social_media import SocialMediaPlatform
from social_media.user import posts


def measure_time(function, *values):
    start_time = time.perf_counter()
    result = function(*values)
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return result, total_time


def main():
    fake = Faker('en_US')

    usernames = [fake.name() for _ in range(100)]
    social_media_platform = SocialMediaPlatform()

    for username in usernames:
        social_media_platform.register_user(username)

    for user in social_media_platform.users.keys():
        users_to_follow = random.sample(usernames, 10)
        if user.username in users_to_follow:
            users_to_follow.remove(user.username)

        for user_to_follow in users_to_follow:
            result, time_taken = measure_time(user.follow, user_to_follow)

    print('\nFollow function time analysis')
    print(f'Time taken to execute follow function is {time_taken} seconds.')

    for user in social_media_platform.users.keys():
        random_num_of_posts = random.randint(1, 10)
        for _ in range(random_num_of_posts):
            result, time_taken = measure_time(user.post_message, fake.text())

    print('\nPost message function time analysis')
    print(f'Time taken to execute post message function is {time_taken} seconds.')

    for user in social_media_platform.users.keys():
        # print(f'User: {user.username}')
        result, time_taken = measure_time(social_media_platform.generate_timeline, user.username)

    print('\nGenerate timeline function time analysis')
    print(f'Time taken to execute generate timeline function is {time_taken} seconds.')


if __name__ == '__main__':
    main()
