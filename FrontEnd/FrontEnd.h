#ifndef FRONTEND_H
#define FRONTEND_H

#include <iostream>
#include <string>
#include "UserSession.h" 
#include "TransactionProcessor.h" 

class FrontEnd {
public:
    FrontEnd();
    void startSession();
    void endSession();
    void simulateTransactions();

private:
    void processUserInput(const std::string& userInput);
    UserSession currentUserSession;
    TransactionProcessor transactionProcessor;
};

#endif // FRONTEND_H
