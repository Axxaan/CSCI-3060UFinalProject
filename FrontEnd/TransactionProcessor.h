#ifndef TRANSACTIONPROCESSOR_H
#define TRANSACTIONPROCESSOR_H

#include <string>
#include "Transaction.h"

class TransactionProcessor {
public:
    void CreateAccount(const std::string& username);
    void SellGame(const std::string& gameName, float price);
    void BuyGame(const std::string& gameName, const std::string& currency, float price);
    void AddCredit(float amount, const std::string& currency);
    void RefundGame(float amount);
    void DeleteAccount(const std::string& username);
};

#endif // TRANSACTIONPROCESSOR_H
