class GameManager:
    @staticmethod
    def add_game_to_collection(game_name, buyer_username, game_collections_file):
        # Appends a game and its new owner to the game collections file.
        with open(game_collections_file, 'a') as file:
            file.write(f"{game_name}______________{buyer_username}_______\n")

    @staticmethod
    def add_game_for_sale(game_name, seller_username, price, available_games_file):
        # Lists a new game for sale in the available games file.
        with open(available_games_file, 'a') as file:
            file.write(f"{game_name}________________{seller_username}________{price:.2f}\n")
