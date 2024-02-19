#ifndef FILEHANDLER_H
#define FILEHANDLER_H

#include <iostream>
#include <fstream>
#include <string>

class FileHandler {
public:
    void readUserAccountsFile();
    void readAvailableGamesFile();
    void writeDailyTransactionFile();
};

#endif // FILEHANDLER_H
