#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For std::find

class ListGames {
private:
    std::vector<std::string> games; // Container for storing game names

public:
    ListGames() {
        // Initialize with some games (optional)
        games = {"Game1: $19.99", "Game2: $24.99", "Game3: $14.99"};
    }

    void listAllGames() {
        std::cout << "3. Game List:" << std::endl;
        for (const auto& game : games) {
            std::cout << "   - " << game << std::endl;
        }
    }

    void listTopGames() {
        // Assuming top games are the first 3, or however you'd like to define "top"
        std::cout << "Listing top games..." << std::endl;
        int count = 0;
        for (const auto& game : games) {
            std::cout << "   - " << game << std::endl;
            if (++count == 3) break; // Only list the top 3 games
        }
    }

    void addGame(const std::string& gameName) {
        games.push_back(gameName);
        std::cout << "Added game: " << gameName << std::endl;
    }

    void removeGame(const std::string& gameName) {
        auto it = std::find(games.begin(), games.end(), gameName);
        if (it != games.end()) {
            games.erase(it);
            std::cout << "Removed game: " << gameName << std::endl;
        } else {
            std::cout << "Game not found: " << gameName << std::endl;
        }
    }
};
