#include <fstream>
#include <string>


std::wstring strToWstringLower(std::string s);

int findWordPair (std::ifstream &file, std::wstring firstWord, std::wstring secondWord, int dist);
