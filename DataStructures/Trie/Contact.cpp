//g++ Contact.cpp -g -std=c++11
//https://www.hackerrank.com/challenges/contacts
// Timeout
#include<string>
#include<iostream>
#include<vector>

using namespace std;


int main() {
    int lines;
    string command;
    string str;
    cin >> lines;
    vector<string> contacts;
    while(lines)
    {
        cin >> command;
        cin >> str;
        if(!command.compare("add"))
            contacts.push_back(str);
        else
        {
            int matches(0);
            for(int i(0); i<contacts.size(); i++)
                if(contacts[i].find(str) != string::npos)
                    matches++;
            cout << matches << endl;
        }
        lines--;
    }
    return 0;
}
