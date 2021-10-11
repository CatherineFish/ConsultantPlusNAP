#include <fstream>
#include <string>
#include <algorithm>
#include "myLibrary.h"
#include <codecvt>
#include <locale> 
#include <functional>
#include <cctype>

#include <iostream>

// function to convert char * to wstring in lowercase
std::wstring strToWstringLower(std::string word)
{
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    //setup converter
    using convert_type = std::codecvt_utf8<typename std::wstring::value_type>;
    std::wstring_convert<convert_type, typename std::wstring::value_type> converter;

    //use converter
    std::wstring wordWString = converter.from_bytes(word);
    
    // transform to lowecase
    std::transform(wordWString.begin(), wordWString.end(), wordWString.begin(), 
                    [](wchar_t c)
                    {
                        return std::tolower<wchar_t>(c, std::locale("ru_RU.UTF-8"));
                    }
    );

    // remove non alpha character in end of word 
    if (!std::isalpha(*std::prev(wordWString.end()), std::locale("ru_RU.UTF-8")))
    {
        wordWString.erase(std::prev(wordWString.end()));
    }

    return wordWString;
}


// function to search for a pair of words at a given distance
int findWordPair (std::ifstream &file, std::wstring firstWord, std::wstring secondWord, int dist)
{
    std::string curWord;
    std::wstring curWString;
    int pairCnt = 0, curDist = -1; // word pair counter and distance counter
    while (file >> curWord)
    {
        curWString = strToWstringLower(curWord);
        if (!curWString.compare(firstWord)) // first word found
        {
            curDist = 0; // start counting the distance
        } else if (!curWString.compare(secondWord)) // second word found
        {
           if (curDist != -1) // found the first word at a distance less than given
           {
                pairCnt++;
                curDist = -1;  // initial state
           }  
        } else
        {
            if (curDist != -1) // found the first word earlier
            {
                curDist++;
            }
            if (curDist > dist) // too many words after first
            {
                curDist = -1;
            }
        }    
    }
    return pairCnt; 
}
