//https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/submissions/code/38064015
//DONE
void Print(Node *head)
{
 while (head)
	{
		cout << head->data << endl;
        head = head->next;
	} 
}