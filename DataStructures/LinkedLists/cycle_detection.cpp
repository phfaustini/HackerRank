//https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle
// DONE
/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    if(head == NULL)
        return false;

    int i(1);
    while(i <= 101)
    {
        head = head->next;
        i++;
        if(head == NULL)
            return false;
    }
    return true;
    
}
