#include<stdio.h>
int main(){
	int a;
	printf("\nEnter a number :\n");
	scanf("%d",&a);
	//'if' statement checks condition  if its true than execute statements associated with it, else move for 'else if' and so on at last 'else' statement(optional)
	if(a>0){
		printf("\nEntered number is positive\n");
	}
	//there can be multipe 'else if' statements
	else if(a<0){
		printf("\nEntered number is negative\n");
	}
	else{
        printf("\nEntered is Zero\n");
	}

	return 0;
}