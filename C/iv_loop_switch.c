#include<stdio.h>
//LIMIT is define as 5,So whenever limit is used tha it replaced by its value 5
#define LIMIT 5
int main()
{
	int i,sum=0;
	//for loop
	//here first i is initailized to 1 .this initialization is done at starting of for loop
	//then it checks whether i<=LIMIT i.e i<=5
	//if true than block of statements of loop are executed than i++ i.e i value is increment by 1
	//for loop statement is executed till condition is true
	for (i=1;i<=LIMIT;i++){
		//for loop statements
		sum+=i;//sum=sum+i
	}
	printf("Sum of first %d Natural number is %d\n",LIMIT,sum );

	int month;
	printf("\nPlease enter valid month in number :\n");
	scanf("%d",&month);
	//in switch 
	//value inside switch(month) i.e month is matched with with value associated with each case 
	//if match is found than value associated with that match is executed  
	//else statement associated with  default is executed
	switch(month){
		case 1:
		    printf("January");
		    break;
		case 2:
		    printf("February");
		    break;
		case 3:
		    printf("March");
		    break;
		case 4:
		    printf("April");
		    break;
		case 5:
		    printf("May");
		    break;
		case 6:
		    printf("June");
		    break;
		case 7:
		    printf("July");
		    break;
		case 8:
		    printf("August");
		    break;
		case 9:
		    printf("September");
		    break;
		case 10:
		    printf("October");
		    break;
		case 11:
		    printf("November");
		    break;
		case 12:
		    printf("December");
		    break;
		default:
		    printf("Sorry you enterdInvalid month enterd");
	}


	return 0;
}