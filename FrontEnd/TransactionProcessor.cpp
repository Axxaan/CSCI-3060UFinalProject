#include <iostream>
#include <string>
#include "Transaction.cpp" 

// TransactionProcessor class

/* The TransactionProcessor class provides a centralized mechanism for handling all types of
transactions in the application, abstrating away the details of the transaction creation and execution.
It promotes maintainability and modularity by seperating transaction processing logic from other parts.*/
class TransactionProcessor {
public:
    // Each of these methods will create and execute a specific transaction type
    void CreateAccount(const std::string& username) {
        CreateAccountTransaction createAccountTransaction(username);
        createAccountTransaction.execute();
    }

    void SellGame(const std::string& gameName, float price) {
        SellTransaction sellTransaction(gameName, price);
        sellTransaction.execute();
    }

    void BuyGame(const std::string& gameName, const std::string& currency,float price) {
        BuyTransaction buyTransaction(gameName, price);
        buyTransaction.execute();
    }

    void AddCredit(float amount, const std::string& currency) {
        AddCreditTransaction addCreditTransaction(amount, currency);
        addCreditTransaction.execute();
    }

    void RefundGame(float amount) {
        RefundTransaction refundTransaction(amount);
        refundTransaction.execute();
    }
    void DeleteAccount(const std::string& username){
        DeleteAccountTransaction deletetransaction(username);
        deletetransaction.execute();
    }

};


