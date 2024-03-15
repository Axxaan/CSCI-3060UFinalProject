import os
import re

class FileManager:
    @staticmethod
    def merge_daily_transactions(daily_transactions_folder_path, output_folder_path):
        # Merges all daily transaction files into a single file.
        merged_transactions_file = os.path.join(output_folder_path, "merged_daily_transactions.txt")
        with open(merged_transactions_file, 'w') as merged_file:
            for filename in os.listdir(daily_transactions_folder_path):
                if filename.startswith("daily_transaction_") and filename.endswith(".txt"):
                    file_path = os.path.join(daily_transactions_folder_path, filename)
                    with open(file_path, 'r') as daily_file:
                        merged_file.write(daily_file.read())

    @staticmethod
    def write_users_to_file(users, file_path):
        # Writes user data to a specified file, appending to it or creating it if not exist.
        with open(file_path, 'a+') as file: #changed 'w' to 'a+' so in this mode will create the file if it doesn't exist, and if it does, it will append to it.
            for username, details in users.items():
                file.write(f"{username}__{details['user_type']}__{details['credit']:.2f}\n")
            file.write("END________________000000.00\n")  # Assuming your file ends with this line
    
    
    @staticmethod
    def load_users(file_path):
        # Loads user data from a file into a dictionary.
        users = {}
        with open(file_path, 'r') as file:
            for line in file:
                if "END" in line:  # Check for the end of the file
                    break
                # Use regex to find groups of non-underscore characters
                parts = re.findall(r'[^_]+', line.strip())
                if len(parts) < 3:
                    continue  # Skip malformed lines
                username, user_type, credit_str = parts
                try:
                    credit = float(credit_str)
                except ValueError as e:
                    print(f"Error converting '{credit_str}' to float: {e}")
                    continue  # Skip this line and continue with the next one
                users[username] = {'user_type': user_type, 'credit': credit}
        return users

    @staticmethod
    def load_games(file_path):
        # Loads game data from a file into a dictionary.
        games = {}
        with open(file_path, 'r') as file:
            for line in file:
                if "END" in line:
                    break
                # Split the line by a large number of underscores, which should be unique separators
                parts = line.split("________________")
                if len(parts) < 3:
                    continue  # Skip malformed lines
                game_name = parts[0]
                seller_username_price = parts[1].split("________")
                if len(seller_username_price) < 2:
                    continue  # Skip malformed lines
                seller_username = seller_username_price[0]
                price_str = seller_username_price[1]
                try:
                    price = float(price_str)
                except ValueError as e:
                    print(f"Error converting '{price_str}' to float: {e}")
                    continue
                games[game_name] = {'seller_username': seller_username, 'price': price}
        return games


    @staticmethod
    def load_game_collections(file_path):
        # Loads game collection data from a file into a dictionary.
        game_collections = {}
        with open(file_path, 'r') as file:
            for line in file:
                if "END" in line:  # Check for the end of the file
                    break
                parts = line.strip().split('_')
                if len(parts) < 3:
                    continue  # Skip malformed lines
                game_name = parts[0]
                buyer_username = parts[1]
                game_collections[game_name] = buyer_username
        return game_collections
