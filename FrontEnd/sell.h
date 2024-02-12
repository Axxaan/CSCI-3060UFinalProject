// sell.h

#ifndef SELL_H
#define SELL_H

#include <string>

class Sell {
public:
    Sell();  // Constructor
    ~Sell(); // Destructor

    void sellGame(const std::string& gameName, float price);
    void displaySuccessMessage();
    void displayErrorMessage();
};

#endif // SELL_H
