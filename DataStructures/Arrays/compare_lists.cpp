//https://www.hackerrank.com/challenges/compare-two-linked-lists
// DONE

/*
  Compare two linked lists A and B
  Return 1 if they are identical and 0 if they are not. 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int CompareLists(Node *headA, Node* headB)
{
    if(!headA && !headB) return 1;

    bool keep = true;
    int equal = 1;

    while(keep)
    {
        if(headA && headB)
        {
            if(headA->data != headB->data)
            {
                equal = 0;
                keep = false;
            }

            headA=headA->next;
            headB=headB->next;
        }
        else if( (headA && !headB) || (!headA && headB))
        {
            keep = false;
            equal = 0;
        }
        else
            keep=false;
    }
    return equal;
}
