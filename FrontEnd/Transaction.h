#ifndef TRANSACTION_H
#define TRANSACTION_H

#include <iostream>
#include <string>

// Base class for transactions
class Transaction {
public:
    virtual void execute() = 0;
    virtual ~Transaction() {}
};
// Subclass for creating an account and it follows the same for the rest below.
class CreateAccountTransaction : public Transaction {
private:
    std::string username;
public:
    CreateAccountTransaction(const std::string& un);
    void execute() override;
};
// Subclass for selling transactions
class SellTransaction : public Transaction {
private:
    std::string gameName;
    float price;
public:
    SellTransaction(const std::string& gn, float p);
    void execute() override;
};

// Subclass for buying transactions
class BuyTransaction : public Transaction {
private:
    std::string gameName;
    float price;
public:
    BuyTransaction(const std::string& gn, float p);
    void execute() override;
};

// Subclass for adding credit
class AddCreditTransaction : public Transaction {
private:
    float amount;
    std::string currency;
public:
    AddCreditTransaction(float amt, const std::string& c);
    void execute() override;
    float CurrencyState(const std::string& c);
};

//Subclass for refund
class RefundTransaction : public Transaction {
private:
    float amount;
public:
    RefundTransaction(float amt);
    void execute() override;
};

//Subclass for deleting account
class DeleteAccountTransaction : public Transaction {
private:
    std::string username;
public:
    DeleteAccountTransaction(const std::string& un);
    void execute() override;
};

#endif // TRANSACTION_H
