// buy.h

#ifndef BUY_H
#define BUY_H

#include <string>

class Buy {
public:
    Buy();   // Constructor
    ~Buy();  // Destructor

    void purchase(const std::string& gameName, float price, std::string& user);
    void displaySuccessMessage();
    void displayErrorMessage();
    void writeToTransaction();
};

#endif // BUY_H
