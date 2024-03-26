import os
import pytest
from UserManager import UserManager
from GameManager import GameManager
from TransactionProcessor import TransactionProcessor
from FileManager import FileManager

def test_merge_daily_transactions(tmpdir):
    daily_transactions_folder = tmpdir.mkdir("daily_transactions")
    output_folder = tmpdir.mkdir("output")

    # Create dummy transaction files
    for i in range(3):
        file = daily_transactions_folder.join(f"daily_transaction_{i}.txt")
        file.write(f"Transaction {i}\n")

    FileManager.merge_daily_transactions(str(daily_transactions_folder), str(output_folder))

    merged_file_path = os.path.join(str(output_folder), "merged_daily_transactions.txt")
    with open(merged_file_path, 'r') as merged_file:
        content = merged_file.read()

    assert content == "Transaction 0\nTransaction 1\nTransaction 2\n"

def test_write_users_to_file(tmpdir):
    file_path = tmpdir.join("users.txt")
    users = {
        "user1": {"user_type": "AA", "credit": 100.00},
        "user2": {"user_type": "FS", "credit": 200.00}
    }
    FileManager.write_users_to_file(users, str(file_path))
    
    with open(file_path) as f:
        content = f.read().splitlines()
    
    assert "user1__AA__100.00" in content
    assert "user2__FS__200.00" in content
    assert "END________________000000.00" in content

def test_load_users(tmpdir):
    file_path = tmpdir.join("users.txt")
    file_path.write("user1__AA__100.00\nuser2__FS__200.00\nEND________________000000.00\n")
    users = FileManager.load_users(str(file_path))
    assert "user1" in users
    assert users["user1"]["user_type"] == "AA"
    assert users["user1"]["credit"] == 100.00
    assert "user2" in users
    assert users["user2"]["user_type"] == "FS"
    assert users["user2"]["credit"] == 200.00

def test_load_game_collections(tmpdir):
    file_path = tmpdir.join("game_collections.txt")
    file_path.write("Game1________________buyer1________\nGame2________________buyer2________\nEND________________000000.00\n")
    game_collections = FileManager.load_game_collections(str(file_path))
    assert "Game1" in game_collections
    assert game_collections.get("Game1") == "buyer1"

# Additional test cases
def test_empty_merge_daily_transactions(tmpdir):
    daily_transactions_folder = tmpdir.mkdir("daily_transactions")
    output_folder = tmpdir.mkdir("output")
    FileManager.merge_daily_transactions(str(daily_transactions_folder), str(output_folder))
    merged_file_path = os.path.join(str(output_folder), "merged_daily_transactions.txt")
    with open(merged_file_path, 'r') as merged_file:
        content = merged_file.read()
    assert content == ""

def test_empty_write_users_to_file(tmpdir):
    file_path = tmpdir.join("empty_users.txt")
    users = {}
    FileManager.write_users_to_file(users, str(file_path))
    with open(file_path) as f:
        content = f.read().splitlines()
    assert content == ["END________________000000.00"]

def test_empty_load_users(tmpdir):
    file_path = tmpdir.join("empty_users.txt")
    file_path.write("END________________000000.00\n")
    users = FileManager.load_users(str(file_path))
    assert users == {}

def test_empty_load_game_collections(tmpdir):
    file_path = tmpdir.join("empty_game_collections.txt")
    file_path.write("END________________000000.00\n")
    game_collections = FileManager.load_game_collections(str(file_path))
    assert game_collections == {}

def test_write_users_to_file_overwrite(tmpdir):
    file_path = tmpdir.join("overwrite_users.txt")
    initial_users = {"user1": {"user_type": "AA", "credit": 50.00}}
    FileManager.write_users_to_file(initial_users, str(file_path))
    new_users = {"user2": {"user_type": "FS", "credit": 150.00}}
    FileManager.write_users_to_file(new_users, str(file_path))
    with open(file_path) as f:
        content = f.read().splitlines()
    assert "user2__FS__150.00" in content
    assert "user1__AA__50.00" not in content

def test_load_users_invalid_format(tmpdir):
    file_path = tmpdir.join("invalid_format_users.txt")
    file_path.write("user1_AA_100.00\nEND________________000000.00\n")
    users = FileManager.load_users(str(file_path))
    assert users == {}


def test_load_game_collections_invalid_format(tmpdir):
    file_path = tmpdir.join("invalid_format_game_collections.txt")
    file_path.write("Game1_buyer1\nEND________________000000.00\n")
    game_collections = FileManager.load_game_collections(str(file_path))
    assert game_collections == {}

def test_write_users_to_file_empty_user(tmpdir):
    file_path = tmpdir.join("empty_user.txt")
    users = {"": {"user_type": "AA", "credit": 0.00}}
    FileManager.write_users_to_file(users, str(file_path))
    with open(file_path) as f:
        content = f.read().splitlines()
    assert "__AA__0.00" in content

def test_load_users_missing_fields(tmpdir):
    file_path = tmpdir.join("missing_fields_users.txt")
    file_path.write("user1__AA\nEND________________000000.00\n")
    users = FileManager.load_users(str(file_path))
    assert users == {}

def test_merge_daily_transactions_no_files(tmpdir):
    daily_transactions_folder = tmpdir.mkdir("empty_daily_transactions")
    output_folder = tmpdir.mkdir("output")
    FileManager.merge_daily_transactions(str(daily_transactions_folder), str(output_folder))
    merged_file_path = os.path.join(str(output_folder), "merged_daily_transactions.txt")
    with open(merged_file_path, 'r') as merged_file:
        content = merged_file.read()
    assert content == ""

def test_load_game_collections_extra_fields(tmpdir):
    file_path = tmpdir.join("extra_fields_game_collections.txt")
    file_path.write("Game1________________buyer1________extra\nEND________________000000.00\n")
    game_collections = FileManager.load_game_collections(str(file_path))
    assert "Game1" in game_collections
    assert game_collections.get("Game1") == "buyer1"    
############################## FileManager.py ########################################################


# Test case 1: Test processing a login transaction
def test_process_login_transaction(capfd):
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    transaction_line = "99_user1"
    result = TransactionProcessor.process_transaction(transaction_line, users, {}, {})
    assert result == "99_user1__buyer__100.00"
    out, _ = capfd.readouterr()
    assert "Login successful for user: user1" in out

# Test case 2: Test processing a logout transaction
def test_process_logout_transaction(capfd):
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    transaction_line = "00_user1"
    result = TransactionProcessor.process_transaction(transaction_line, users, {}, {})
    assert result == "00_user1__buyer__100.00"
    out, _ = capfd.readouterr()
    assert "Logout successful for user: user1" in out

# Test case 3: Test processing a create user transaction
def test_process_create_user_transaction(capfd):
    users = {}
    transaction_line = "01_user1__seller__50.00"
    result = TransactionProcessor.process_transaction(transaction_line, users, {}, {})
    assert result == "01_user1__seller__50.00"
    out, _ = capfd.readouterr()
    assert "User user1 created successfully." in out

# Test case 4: Test processing a delete user transaction
def test_process_delete_user_transaction(capfd):
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    transaction_line = "02_user1"
    result = TransactionProcessor.process_transaction(transaction_line, users, {}, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "User user1 deleted successfully." in out

# Test case 5: Test processing a sell transaction
def test_process_sell_transaction(capfd):
    users = {}
    games = {}
    transaction_line = "03_game1__seller1__20.50"
    result = TransactionProcessor.process_transaction(transaction_line, users, games, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "Game game1 listed for sale by seller1 at $20.50." in out

# Test case 6: Test processing a buy transaction
def test_process_buy_transaction(capfd):
    users = {"buyer1": {"user_type": "buyer", "credit": 50.00}, "seller1": {"user_type": "seller", "credit": 0.00}}
    games = {"game1": {"seller": "seller1", "price": 25.00}}
    transaction_line = "04_game1__buyer1__25.00"
    result = TransactionProcessor.process_transaction(transaction_line, users, games, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "buyer1 bought game1 from seller1. Transaction complete." in out

# Test case 7: Test processing a refund transaction
def test_process_refund_transaction(capfd):
    users = {"user1": {"user_type": "buyer", "credit": 100.00}, "user2": {"user_type": "buyer", "credit": 200.00}}
    transaction_line = "05_user1_user2__50.00"
    result = TransactionProcessor.process_transaction(transaction_line, users, {}, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "Refund successful for user: user1. New credit: 150.00" in out
    assert "Refund successful for user: user2. New credit: 250.00" in out

# Test case 8: Test processing an invalid transaction
def test_process_invalid_transaction(capfd):
    users = {}
    transaction_line = "99_user1_invalid"
    result = TransactionProcessor.process_transaction(transaction_line, users, {}, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "Invalid transaction format for refund: 99_user1_invalid" in out

# Test case 9: Test processing a transaction with insufficient credit for purchase
def test_process_insufficient_credit_transaction(capfd):
    users = {"buyer1": {"user_type": "buyer", "credit": 20.00}}
    games = {"game1": {"seller": "seller1", "price": 25.00}}
    transaction_line = "04_game1__buyer1__25.00"
    result = TransactionProcessor.process_transaction(transaction_line, users, games, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "buyer1 does not have enough credit to buy game1." in out

# Test case 10: Test processing a purchase of a non-existent game
def test_process_non_existent_game_transaction(capfd):
    users = {"buyer1": {"user_type": "buyer", "credit": 50.00}}
    games = {}
    transaction_line = "04_game1__buyer1__25.00"
    result = TransactionProcessor.process_transaction(transaction_line, users, games, {})
    assert result is None
    out, _ = capfd.readouterr()
    assert "game1 is not available for purchase." in out
    
    
# Test case 1: Test modifying user credit for an existing user
def test_modify_user_credit_existing_user():
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    username = "user1"
    credit_change = 50.00
    UserManager.modify_user_credit(username, credit_change, users)
    assert users["user1"]["credit"] == 150.00

# Test case 2: Test modifying user credit for a non-existing user
def test_modify_user_credit_non_existing_user(capfd):
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    username = "user2"
    credit_change = 50.00
    UserManager.modify_user_credit(username, credit_change, users)
    assert users["user2"] == {"user_type": "buyer", "credit": 50.00}

# Test case 3: Test adding a new user to the system
def test_add_user_to_system():
    users = {}
    username = "new_user"
    user_type = "seller"
    credit = 50.00
    system_accounts_file = "system_accounts_test.txt"
    UserManager.add_user_to_system(username, user_type, credit, system_accounts_file)
    assert os.path.exists(system_accounts_file)
    with open(system_accounts_file, 'r') as file:
        lines = file.readlines()
        assert f"{username}__{user_type}__{credit:.2f}\n" in lines

# Test case 4: Test adding a new user to the system with an existing user
def test_add_existing_user_to_system():
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    username = "user1"
    user_type = "seller"
    credit = 50.00
    system_accounts_file = "system_accounts_test.txt"
    UserManager.add_user_to_system(username, user_type, credit, system_accounts_file)
    assert os.path.exists(system_accounts_file)
    with open(system_accounts_file, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 1  # Ensure only one line added for existing user

# Test case 5: Test modifying user credit by a negative value
def test_modify_user_credit_negative_value():
    users = {"user1": {"user_type": "buyer", "credit": 100.00}}
    username = "user1"
    credit_change = -50.00
    UserManager.modify_user_credit(username, credit_change, users)
    assert users["user1"]["credit"] == 50.00

# Test case 6: Test modifying user credit for multiple users
def test_modify_user_credit_multiple_users():
    users = {"user1": {"user_type": "buyer", "credit": 100.00}, "user2": {"user_type": "seller", "credit": 50.00}}
    username = "user1"
    credit_change = 25.00
    UserManager.modify_user_credit(username, credit_change, users)
    assert users["user1"]["credit"] == 125.00
    assert users["user2"]["credit"] == 50.00

# Test case 7: Test adding multiple users to the system
def test_add_multiple_users_to_system():
    users = {}
    usernames = ["new_user1", "new_user2"]
    user_type = "buyer"
    credit = 100.00
    system_accounts_file = "system_accounts_test.txt"
    for username in usernames:
        UserManager.add_user_to_system(username, user_type, credit, system_accounts_file)
    assert os.path.exists(system_accounts_file)
    with open(system_accounts_file, 'r') as file:
        lines = file.readlines()
        for username in usernames:
            assert f"{username}__{user_type}__{credit:.2f}\n" in lines

# Test case 8: Test modifying credit for an empty user dictionary
def test_modify_user_credit_empty_users():
    users = {}
    username = "user1"
    credit_change = 50.00
    UserManager.modify_user_credit(username, credit_change, users)
    assert users == {}

# Test case 9: Test adding a new user with a negative credit value
def test_add_user_to_system_negative_credit():
    users = {}
    username = "new_user"
    user_type = "seller"
    credit = -50.00
    system_accounts_file = "system_accounts_test.txt"
    UserManager.add_user_to_system(username, user_type, credit, system_accounts_file)
    assert os.path.exists(system_accounts_file)
    with open(system_accounts_file, 'r') as file:
        lines = file.readlines()
        assert f"{username}__{user_type}__{credit:.2f}\n" not in lines

# Test case 10: Test adding a new user with a user type that is not 'buyer' or 'seller'
def test_add_user_to_system_invalid_user_type():
    users = {}
    username = "new_user"
    user_type = "invalid_type"
    credit = 50.00
    system_accounts_file = "system_accounts_test.txt"
    UserManager.add_user_to_system(username, user_type, credit, system_accounts_file)
    assert os.path.exists(system_accounts_file)
    with open(system_accounts_file, 'r') as file:
        lines = file.readlines()
        assert f"{username}__{user_type}__{credit:.2f}\n"
        
        
# Test case 1: Test adding a game to the collection
def test_add_game_to_collection(tmpdir):
    game_collections_file = tmpdir.join("game_collections.txt")
    GameManager.add_game_to_collection("Game1", "buyer1", str(game_collections_file))
    assert os.path.isfile(str(game_collections_file))

# Test case 2: Test adding a game for sale
def test_add_game_for_sale(tmpdir):
    available_games_file = tmpdir.join("available_games.txt")
    GameManager.add_game_for_sale("Game1", "seller1", 10.50, str(available_games_file))
    assert os.path.isfile(str(available_games_file))

# Test case 3: Test adding a game to the collection with special characters in the game name and buyer username
def test_add_game_to_collection_special_characters(tmpdir):
    game_collections_file = tmpdir.join("game_collections.txt")
    GameManager.add_game_to_collection("Game!@#", "buyer!@#", str(game_collections_file))
    assert os.path.isfile(str(game_collections_file))

# Test case 4: Test adding a game for sale with special characters in the game name and seller username
def test_add_game_for_sale_special_characters(tmpdir):
    available_games_file = tmpdir.join("available_games.txt")
    GameManager.add_game_for_sale("Game!@#", "seller!@#", 10.50, str(available_games_file))
    assert os.path.isfile(str(available_games_file))

# Test case 5: Test adding a game to the collection with an empty game name and buyer username
def test_add_game_to_collection_empty(tmpdir):
    game_collections_file = tmpdir.join("game_collections.txt")
    GameManager.add_game_to_collection("", "", str(game_collections_file))
    assert os.path.isfile(str(game_collections_file))

# Test case 6: Test adding a game for sale with an empty game name and seller username
def test_add_game_for_sale_empty(tmpdir):
    available_games_file = tmpdir.join("available_games.txt")
    GameManager.add_game_for_sale("", "", 10.50, str(available_games_file))
    assert os.path.isfile(str(available_games_file))

# Test case 7: Test adding a game to the collection with a long game name and buyer username
def test_add_game_to_collection_long(tmpdir):
    game_collections_file = tmpdir.join("game_collections.txt")
    GameManager.add_game_to_collection("A" * 1000, "B" * 1000, str(game_collections_file))
    assert os.path.isfile(str(game_collections_file))

# Test case 8: Test adding a game for sale with a long game name and seller username
def test_add_game_for_sale_long(tmpdir):
    available_games_file = tmpdir.join("available_games.txt")
    GameManager.add_game_for_sale("A" * 1000, "B" * 1000, 10.50, str(available_games_file))
    assert os.path.isfile(str(available_games_file))

# Test case 9: Test adding multiple games to the collection
def test_add_multiple_games_to_collection(tmpdir):
    game_collections_file = tmpdir.join("game_collections.txt")
    GameManager.add_game_to_collection("Game1", "buyer1", str(game_collections_file))
    GameManager.add_game_to_collection("Game2", "buyer2", str(game_collections_file))
    assert os.path.isfile(str(game_collections_file))

# Test case 10: Test adding multiple games for sale
def test_add_multiple_games_for_sale(tmpdir):
    available_games_file = tmpdir.join("available_games.txt")
    GameManager.add_game_for_sale("Game1", "seller1", 10.50, str(available_games_file))
    GameManager.add_game_for_sale("Game2", "seller2", 20.75, str(available_games_file))
    assert os.path.isfile(str(available_games_file))