#include <iostream>
#include <string>
#include "UserSession.cpp"
#include "TransactionProcessor.cpp"

// FrontEnd Class
/* This class provides a user-friendly interface for interacting with the app. It allows other
users to perform other transactions such as buying/selling games, making accounts, adding credits
and refunding games.*/
class FrontEnd {
public:
    FrontEnd() {
        // Constructor can initialize components if needed
    }

    void startSession() {
        std::cout << "Session started.\n";
    }

    void endSession() {
        std::cout << "Session ended.\n";
    }

    // Method to simulate transactions based on user input
    void simulateTransactions() {
        std::cout << "Menu:\n";
        std::cout << "1. Create Account\n";
        std::cout << "2. Sell Game\n";
        std::cout << "3. Buy Game\n";
        std::cout << "4. Add Credit\n";
        std::cout << "5. Refund Game\n";
        std::cout << "6. Login\n";
        std::cout << "7. Delete Account\n";
        std::cout << "Enter your choice: ";
        
        std::string userInput;
        do {
            std::cout << "Enter a transaction or 'exit' to quit and log off: ";
            std::getline(std::cin, userInput);
            
            if (userInput == "exit") {
                break;
            } else if (userInput == "6") { // Check if user wants to login
                currentUserSession.login("exampleUser"); 
            } else {
                // Call appropriate methods of TransactionProcessor based on user input
                processUserInput(userInput);
            }
        } while (userInput != "exit");
        
        currentUserSession.logout();
    }

    void processUserInput(const std::string& userInput) {
        // Parse user input as integer
        int choice;
        try {
            choice = std::stoi(userInput);
        } catch (...) {
            std::cout << "Invalid input. Please enter a number.\n";
            return;
        }

        // Call corresponding methods of TransactionProcessor based on user choice
        switch (choice) {
            case 1:
                transactionProcessor.CreateAccount("exampleUser");
                break;
            case 2:
                transactionProcessor.SellGame("CoolGame", 19.99f);
                break;
            case 3:
                transactionProcessor.BuyGame("CoolGame", "CAD", 19.99f);
                transactionProcessor.BuyGame("CoolGameUS", "USD", 19.99f);
                break;
            case 4:
                transactionProcessor.AddCredit(100.0f, "CAD");
                break;
            case 5:
                transactionProcessor.RefundGame(19.99f);
                break;
            case 7:
                transactionProcessor.DeleteAccount("exampleUser");
                break;
            default:
                std::cout << "Invalid choice. Please enter a valid number.\n";
                break;
        }
    }

private:
    UserSession currentUserSession;
    TransactionProcessor transactionProcessor;
};

int main(int argc, char* argv[]) {
    //simulating the whole project
   // FrontEnd frontEnd;
   // frontEnd.startSession();
   // frontEnd.simulateTransactions();
   // frontEnd.endSession();
    if (argc != 5) {
    std::cerr << "Usage: " << argv[0] << " currentaccounts.txt availablegames.txt gamescollection.txt transout.atf" << std::endl;
    return 1;
    }

    std::string currentAccountsFile = argv[1];
    std::string availableGamesFile = argv[2];
    std::string gamesCollectionFile = argv[3];
    std::string transactionOutputFile = argv[4];

    return 0;
};