#include<stdio.h>             //include information about standard library.'stdio.h' is standard input output (library)header file  that stores pre-defined function like printf(),scanf() etc
int main()                    //define function named main() .Execution of C program starts from main()    
{
	printf("hello, world\n"); //main() calls library function printf to print sequence of characters
	                          //'\n' represent the newline
	return 0;                 //since main() is defined as int ,so it will return a value.And 'return 0' represent  end of execution
}