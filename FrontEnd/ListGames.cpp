#include <iostream>
#include <vector>
#include <string>

// ListGames class
/* This class is responsible for listing games within an application, providing functionality to list
all different games and top games*/
class ListGames {
public:
    void listAllGames() {
        std::cout << "Listing all games..." << std::endl;
        // Placeholder for listing all games logic
    }

    void listTopGames() {
        std::cout << "Listing top games..." << std::endl;
        // Placeholder for listing top games logic
    }

    void addGame(const std::string& gameName) {
        // Placeholder for adding game
        std::cout << "Added game: " << gameName << std::endl;
    }
    void removeGame(const std::string& gameName) {
        // Placeholder for removing game
        std::cout << "Removed game: " << gameName << std::endl;
    }
};
