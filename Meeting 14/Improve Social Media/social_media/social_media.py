from social_media.user import User, posts


class SocialMediaPlatform:
    def __init__(self):
        """
        Initialize the social media platform with 0 users
        """
        # self.users = []
        self.users = {}

    # Old Runtime: O(n ^ 2)
    # New Runtime: O(1)
    def register_user(self, username):
        """
        Register a new user and add it to the users list
        :param username: The users username to add
        :return: None
        """
        # if not self._is_username_taken(username):
        #     user = User(username)
        #     self.users.append(user)
        if username not in self.users.values():
            user = User(username)
            self.users[user] = username

    # # Old Runtime: O(n)
    # # New Runtime: 0
    # def _is_username_taken(self, username):
    #     """
    #     Check if the username is already taken
    #     :param username: The username to check
    #     :return: True if the username is already taken, False otherwise
    #     """
    #     for user in self.users:
    #         if user.username == username:
    #             return True
    #     return False

    # Old Runtime: O(n)
    # New Runtime: O(n)
    def get_user_by_username(self, username):
        """
        Retrieve the user with the given username
        :param username: The username to retrieve
        :return: The user with the given username or None if no such user is found
        """
        # for user in self.users:
        #     if user.username == username:
        #         return user
        # return None
        for key, value in self.users.items():
            if value == username:
                return key
        return None

    # Old Runtime: O(n ^ 3)
    # New Runtime: O(n)
    def generate_timeline(self, username):
        """
        Generate a timeline for the given user
        :param username: The username to generate a timeline for
        :return: Empty timeline if no such user is found for the given username or the timeline for the given user if found
        """
        user = self.get_user_by_username(username)
        if not user:
            return {}

        timeline = {}
        for followed_user in user.following.keys():
            timeline[followed_user] = posts[followed_user]
        # for followed_user in user.following:
        #     for post in posts:
        #         if post['username'] == followed_user:
        #             timeline.append(post)
        return timeline
