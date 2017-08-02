#include<stdio.h>
int main(){
	//arr is collection of data of same data type
	int a[10]={5,8,11,16,20,25,35,48,55,68};//a[] is array of 10 data of type integer
	//a[10] mean there 10 integer i.e a[0],a[1],a[2],a[3],a[4]...a[9]
	int find;
	printf("\n=========while Loop implementation=========\n");
	
	printf("\nEnter interger which you want to find\n");
	scanf("%d",&find);
	int i=0;
	//in while loop it check foe condition
	//if it is true than it execute block of statements of loop
	//else loop terminate
	while(a[i]!=find && i<10){
		i++;
	}
	if(a[i]==find){
		printf("\nNumber is found at %d position \n",i);
	}
	else{
		printf("\nNot Found\n");
	}

	printf("\n=========do-while Loop implementation=========\n");
	int x,y,temp;
	printf("\nEnter two number\n");
	scanf("%d %d",&x,&y);
    //in do-while first it executes block of statements and than checks condition 
    //if it is true than it again execute block of statement
    //else terminate
	do{
		temp=x%y;
		x=y;
		y=temp;

	}while(y>0);
	printf("\nGCD of Entered number is %d\n",x);

	return 0;
}