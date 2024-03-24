class User:
    def __init__(self, username):
        """
        Create a user with a username and a list of the users he follows
        :param username:
        """
        self.username = username
        self.following = []

    # Old Runtime: O(n ^ 2)
    def follow(self, other_user):
        """
        Add a user to the list of users that the current user follows
        :param other_user: The user to add
        :return: None
        """
        if other_user not in self.following:
            self.following.append(other_user)

    # Old Runtime: O(n)
    def post_message(self, message):
        """
        Add a post to the list of posts of the current user
        :param message: The post to add
        :return: None
        """
        post = {'username': self.username, 'message': message}
        posts.append(post)


# Assume posts are stored in a global list
posts = []
