//https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
// DONE
/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
    Node *n = new Node;
    n->data = data;
    n->next = NULL;
    if(!head) return n;

    if(position == 0)
    {
        n->next = head;
        return n;
    }

    Node *cursorB = head;
    Node *cursorA = head->next;
    position--;
    while(position > 0)
    {
        position--;
        cursorB = cursorB->next;
        cursorA = cursorA->next;
    }
    n->next = cursorA;
    cursorB->next = n;

    return head;
}