class UserManager:
    @staticmethod
    def modify_user_credit(username, credit_change, users):
        # Updates a user's credit by credit_change amount and prints success or failure message.
        if username in users:
            users[username]['credit'] += credit_change
            print(f"Refund successful for user: {username}. New credit: {users[username]['credit']:.2f}")
        else:
            print(f"Refund failed: User {username} not found.")
        return users

    @staticmethod
    def add_user_to_system(username, user_type, credit, system_accounts_file):
        # Adds a new user to system_accounts_file with provided details.
        with open(system_accounts_file, 'a') as file:
            file.write(f"{username}__{user_type}__{credit:.2f}\n")
