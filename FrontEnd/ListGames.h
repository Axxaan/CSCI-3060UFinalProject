#ifndef LISTGAMES_H
#define LISTGAMES_H

#include <iostream>
#include <vector>
#include <string>

class ListGames {
public:
    void listAllGames();
    void listTopGames();
    void addGame(const std::string& gameName);
    void removeGame(const std::string& gameName);
};

#endif // LISTGAMES_H
