//https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse
// DONE
#include<stack>

/*
  Print elements of a linked list in reverse order as standard output
  head pointer could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
void ReversePrint(Node *head)
{   
    stack<int> s;
    while(head)
    {
        s.push(head->data);
        head = head->next;
    }
    while(!s.empty())
    {
        cout << s.top() << endl;
        s.pop();
    }
}
