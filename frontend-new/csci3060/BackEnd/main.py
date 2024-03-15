from TransactionProcessor import TransactionProcessor
from UserManager import UserManager
from GameManager import GameManager
from FileManager import FileManager

def main():
    # Loading up each of the files 
    FileManager.merge_daily_transactions("D:/CSCI-3060UFinalProject-3/frontend-new/csci3060/storage/daily_transactions", "D:/CSCI-3060UFinalProject-3/frontend-new/csci3060/storage")
    users = FileManager.load_users('D:/CSCI-3060UFinalProject-3/frontend-new/csci3060/storage/current_user_accounts.txt')
    games = FileManager.load_games('D:/CSCI-3060UFinalProject-3/frontend-new/csci3060/storage/available_games.txt')
    game_collections = FileManager.load_game_collections('D:/CSCI-3060UFinalProject-3/frontend-new/csci3060/storage/game_collection.txt')
    transactions = []

    with open('D:/CSCI-3060UFinalProject-3/frontend-new/csci3060/storage/merged_daily_transactions.txt', 'r') as file:
        transactions = [line.strip() for line in file.readlines()]
    
    for transaction_line in transactions:
        response = TransactionProcessor.process_transaction(transaction_line, users, games, game_collections)
        if response:
            print(response)

if __name__ == '__main__':
    main()
