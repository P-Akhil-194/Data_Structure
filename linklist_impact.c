#include<stdio.h>

struct node{
	int val;	
	struct node *ptr;
};

int main(){
	struct node n1,n2,n3,*head = NULL,*temp = NULL;
		
	n1.val = 10;
	n1.ptr = NULL;
	n2.val = 20;
	n2.ptr = NULL;
	n3.val = 30;
	n3.ptr = NULL;
	
	// new node inserting between n2 and n3
	struct node n4;
	n4.val = 40;
	n4.ptr = NULL;
		
	//make a relationshilp
	n1.ptr = &n2;
	n2.ptr = &n3;
	
	// making the relation of new node
	n4.ptr = &n3;
	n2.ptr = &n4;
	
	//assign the base address to the head
	head = &n1;
	temp = head;
	
	//print
//	printf("%d->",head->val);
//	head = head -> ptr;
//	printf("%d->",head->val);
//	head = head -> ptr;
//	printf("%d->",head->val);
// second way of printing
	while(head != NULL){
		printf("%d->",head->val);
		head = head -> ptr;
	}
	if (head == NULL){
		printf("None");
	}
	return 0;
}
