from domain.user import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

class InMemoryUserRepository:
    def __init__(self):
        self.users = {
            1: User(1, 'Alice', 'alice@example.com'),
            2: User(2, 'Bob', 'bob@example.com'),
            3: User(3, 'Charlie', 'charlie@example.com'),
        }

    def get_user(self, user_id):
        return self.users.get(user_id)