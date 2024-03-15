from UserManager import UserManager
from FileManager import FileManager
from GameManager import GameManager

class TransactionProcessor:
    TRANSACTION_CODE_MAP = {
        '99': 'login',
        '00': 'logout',
        '01': 'create_user',
        '02': 'delete_user',
        '03': 'sell',
        '04': 'buy',
        '05': 'refund',
        # Add more mappings as needed
    }

    @staticmethod 
    def process_transaction(transaction_line, users, games, game_collections): # Method to process transactions
        parts = transaction_line.strip().split('_')
        transaction_code = parts[0]
        operation = TransactionProcessor.TRANSACTION_CODE_MAP.get(transaction_code, 'invalid')
        
        if operation == 'login':
            # Perform login operation
            # Assuming parts[1] is username
            username = parts[1]
            if username in users:
                user = users[username]
                print(f"Login successful for user: {username}")
                return f"99_{username}__{user['user_type']}__{user['credit']:.2f}"
            else:
                print("Login failed: User not found.")

        elif operation == 'logout':
            # Perform logout operation
            # Assuming parts[1] is username for logout operation
            username = parts[1]
            if username in users:
                print(f"Logout successful for user: {username}")
                # Here you would typically update the user's session state
                return f"00_{username}__{users[username]['user_type']}__{users[username]['credit']:.2f}"
            else:
                print(f"Logout failed: User {username} not found.")
        
        elif operation == 'create_user':
            username = parts[1]
            user_type = parts[2]
            credit = float(parts[3])
            # Check if user already exists
            if username in users:
                print(f"Error: User {username} already exists.")
            else:
                # Assuming 'system_user_accounts.txt' is your system accounts file
                UserManager.add_user_to_system(username, user_type, credit, 'system_user_accounts.txt')
                print(f"User {username} created successfully.")
                return f"01_{username}__{user_type}__{credit:.2f}"
        
        elif operation == 'delete_user':
            username = parts[1]  # Assuming the username to be deleted is the first part after the operation code
            if username in users:
                del users[username]  # Delete the user from the dictionary
                print(f"User {username} deleted successfully.")
                FileManager.write_users_to_file(users, 'system_user_accounts.txt')  # Update the file with the remaining users
            else:
                print(f"Error: User {username} does not exist.")  # User was not found in the dictionary

        
        elif operation == 'sell':
            game_name = parts[1]
            seller_username = parts[2]
            price = float(parts[3])

            # Check if the game is already listed for sale
            if game_name not in games:
                # Add the game to the available games list
                GameManager.add_game_for_sale(game_name, seller_username, price, 'available_games.txt')
                print(f"Game {game_name} listed for sale by {seller_username} at ${price:.2f}.")
                # Optionally, update the games dictionary in-memory if further processing is needed
                games[game_name] = {'seller': seller_username, 'price': price}
            else:
                print(f"Error: Game {game_name} is already listed for sale.")
        
        elif operation == 'buy':
            game_name = parts[1]
            buyer_username = parts[2]
            game_price = float(parts[3])

            # Check if the game exists in the available games
            if game_name in games:
                if users[buyer_username]['credit'] >= games[game_name]['price']:
                    # Deduct the game price from the buyer's credit and update the seller's credit
                    users[buyer_username]['credit'] -= games[game_name]['price']
                    seller_username = games[game_name]['seller']
                    users[seller_username]['credit'] += games[game_name]['price']

                    # Remove the game from available games (if necessary) and add it to the buyer's game collection
                    GameManager.add_game_to_collection(game_name, buyer_username, 'system_game_collection.txt')

                    # Update the system accounts file with the new user credits
                    FileManager.write_users_to_file(users, 'system_user_accounts.txt')
                    print(f"{buyer_username} bought {game_name} from {seller_username}. Transaction complete.")
                else:
                    print(f"{buyer_username} does not have enough credit to buy {game_name}.")
            else:
                print(f"{game_name} is not available for purchase.")
        
        elif operation == 'refund':
            # Attempt to identify the credit change value based on the transaction format
            try:
                # Assuming the last part is always the credit change
                credit_change = float(parts[-1])
                # All parts except the first (transaction code) and last (credit change) are usernames
                usernames = parts[1:-1]
            except ValueError:
                # Log an error if the conversion fails - indicating an improperly formatted transaction
                print(f"Error: Invalid transaction format for refund: {transaction_line}")
                return None

            # Process refund for each username found in the transaction
            for username in usernames:
                if username in users:
                    # Apply the credit change
                    users[username]['credit'] += credit_change
                    print(f"Refund successful for user: {username}. New credit: {users[username]['credit']:.2f}")
                else:
                    print(f"Refund failed: User {username} not found.")

            # After processing refunds, update the system accounts file
            FileManager.write_users_to_file(users, 'system_user_accounts.txt')  # Adjust the file path as necessary



        # Return None or an appropriate string for operations that do not require a response
        return None