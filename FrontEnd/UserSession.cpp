#include <iostream>
#include <string>
//UserSession Class

/* This class provides basic functionality for managing user sessions such as login, logout.
It is used alongside other classes to control access to certain features based on user's login*/
class UserSession {
private:
    std::string currentUserType;
    bool isLoggedIn;

public:
    UserSession() : isLoggedIn(false) {}

    bool login(const std::string& username) {
        // Placeholder for login logic.
        // If login is successful:
        isLoggedIn = true;
        std::cout << "User " << username << " logged in" << std::endl;
        return isLoggedIn;
    }

    void logout() {
        // Placeholder for logout logic.
        isLoggedIn = false;
        currentUserType.clear();
        std::cout << "User logged out." << std::endl;
    }

};
