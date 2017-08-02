#include<stdio.h>
int main()
{
	//declaring variable a,b of integer type
	int a,b;
	//declaring variable ch of character type
	char ch;
	//declaring variable f1,f2 of floating point type
	float f1,f2;

	printf("\nEnter Character:\n");
	//scanf() is input function in stdio.h library
	//%c is field format to take character as input
	//input charcter is stored at location of ch
	scanf("%c",&ch);

	printf("\nEnter two number :\n");
	//%d is field format for integer
	scanf("%d %d",&a,&b);

	printf("\nEnter two floating point number :\n");
	//%f is field format for floating point number
	scanf("%f %f",&f1,&f2);

	//here each %d or field format is replacesd by  variable value respectively
	printf("\nSum of %d and %d is %d\n",a,b,a+b);
	//Or
	//int c=a+b;
	//printf("\nSum of %d and %d is %d\n",a,b,c);

    //here at %d Ascii value of ch is replaced 
	printf("\nASCII value of %c is %d\n",ch,ch);
	//or
	//int d=ch;
	//printf("\nASCII value of %c is %d\n",ch,d);

	printf("\n%f * %f = %f\n",f1,f2,f1*f2);

	printf("\n%0.2f * %0.3f = %0.4f\n",f1,f2,f1*f2);
	return 0;
}