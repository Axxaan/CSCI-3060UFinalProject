#ifndef USERSESSION_H
#define USERSESSION_H

#include <iostream>
#include <string>

class UserSession {
private:
    std::string currentUserType;
    bool isLoggedIn;

public:
    UserSession();
    bool login(const std::string& username);
    void logout();
};

#endif // USERSESSION_H
