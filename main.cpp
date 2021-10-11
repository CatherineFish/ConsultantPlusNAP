#include <iostream>
#include <fstream>
#include <string>
#include <ios>
#include "myLibrary.h"


int main (int argc, char *argv[])//бесконечный ввод
{
    // checking argument number
    if (argc < 5) 
    {
        std::cout << "Incorrect number of arguments" << std::endl;
        return 0; // correct end of app, but with error message for user   
    }

    // file opening
    std::ifstream file;
    file.open(argv[1], std::ios::in);
    if (!file.is_open())
    {
        std::cout << "Incorrect file name" << std::endl;
        return 0; // correct end of app, but with error message for user   

    }

    // converting input words to a lowercase strings
    std::wstring firstWord, secondWord;
    firstWord = strToWstringLower(std::string(argv[2]));
    secondWord = strToWstringLower(std::string(argv[3]));
    
    // main path of app
    std::cout << findWordPair (file, firstWord, secondWord, std::atoi(argv[4])) << std::endl;

    //file closing and the end of app
    file.close();     
    return 0;
}