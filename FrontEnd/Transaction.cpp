#include <iostream>
#include <string>

/*This file defines a set of transaction classes derived from a base class called Transaction. Each transaction class 
represents a specific type of transaction that can occur in an application as well as it implements the execute() method.
This is pure vital function in the base class. It's job is to execute specifc logic with each
type of transaction. */
class Transaction {
public:
    virtual void execute() = 0; // Pure virtual function for executing the transaction
};

// Subclass for creating an account
class CreateAccountTransaction : public Transaction {
private:
    std::string username;
public:
    CreateAccountTransaction(const std::string& un) : username(un) {}
    void execute() override {
        std::cout << "Account created for user: " << username << std::endl;
        // Insert account creation logic here
    }
};

// Subclass for selling transactions
class SellTransaction : public Transaction {
private:
    std::string gameName;
    float price;
public:
    SellTransaction(const std::string& gn, float p) : gameName(gn), price(p) {}
    void execute() override {
        std::cout << "Game " << gameName << " sold for $" << price << std::endl;
        // Insert sell game logic here
    }
};

// Subclass for buying transactions
class BuyTransaction : public Transaction {
private:
    std::string gameName;
    float price;
public:
    BuyTransaction(const std::string& gn, float p) : gameName(gn), price(p) {}
    void execute() override {
        std::cout << "Game " << gameName << " purchased for $" << price << std::endl;
        // Insert buy game logic here
    }
};

// Subclass for adding credit
class AddCreditTransaction : public Transaction {
private:
    float amount;
    std::string currency;
public:
    AddCreditTransaction(float amt, const std::string& c) : amount(amt), currency(c) {}
    void execute() override {
        std::cout << amount << " credits added." << std::endl;
        // Insert add credit logic here
    }

        float CurrencyState(const std::string& c) {
        if ("USD" ==  c)
        {
            return 1.348*amount;
        }
        else
        {
            return amount;
        }
    }
};

// Subclass for refund transactions
class RefundTransaction : public Transaction {
private:
    float amount;
public:
    RefundTransaction(float amt) : amount(amt) {}
    void execute() override {
        std::cout << amount << " refunded." << std::endl;
        // Insert refund logic here
    }
};

// Subclass for creating an account
class DeleteAccountTransaction : public Transaction {
private:
    std::string username;
public:
    DeleteAccountTransaction(const std::string& un) : username(un) {}
    void execute() override {
        std::cout << "Account deleted for user: " << username << std::endl;
        // account delete logic
    }
};

