import os

class FileManager:
    @staticmethod
    def merge_daily_transactions(input_folder, output_folder):
        transactions = []
        for file_name in os.listdir(input_folder):
            file_path = os.path.join(input_folder, file_name)
            with open(file_path, 'r') as file:
                transactions.append(file.read())

        merged_file_path = os.path.join(output_folder, "merged_daily_transactions.txt")
        with open(merged_file_path, 'w') as merged_file:
            for transaction in transactions:
                merged_file.write(transaction)

    @staticmethod
    def write_users_to_file(users, file_path):
        with open(file_path, 'w') as file:
            for username, data in users.items():
                file.write(f"{username}__{data['user_type']}__{data['credit']:.2f}\n")
            file.write("END________________000000.00\n")

    @staticmethod
    def load_users(file_path):
        users = {}
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split("__")
                if len(parts) == 3:
                    username = parts[0]
                    user_type = parts[1]
                    credit = float(parts[2])
                    users[username] = {"user_type": user_type, "credit": credit}
        return users
    
    @staticmethod
    def load_game_collections(file_path):
        game_collections = {}
        with open(file_path, 'r') as file:
            for line in file:
                if "END" in line:
                    break
                parts = line.strip().split('_')
                if len(parts) < 3:
                    continue
                game_name = parts[0]
                buyer_username = parts[1]
                game_collections[game_name] = buyer_username
        return game_collections



