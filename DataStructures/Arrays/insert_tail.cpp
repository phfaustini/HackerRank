//https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
// DONE
/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data)
{
    Node *n = new Node;
    if(!head)
    {
        n->data = data;
        n->next = NULL;
        return n;
    }
    else
    {
        Node *cursor = head;
        while(cursor->next)
            cursor = cursor->next;
        n->data = data;
        n->next = NULL;
        cursor->next = n;

        return head;
    }
}