#include<stdio.h>
#define MAXLINE 1000  /*maximum input line length*/
//deeclaration of function
//syntax 
//return-type function-name(data-tye argument-name,...);
int getlines(char line[],int max);
int strindex(char source[],char searchfor[]);

//global variable ,i.e accessed by all function
char pattern[]="ould"; 
int main(){

	int found=0;
	char line[MAXLINE];
	//calling function getline()
	//here starting address of array line[] is passed as first parameter(arguement)
    while(getlines(line,MAXLINE)>0){
    	//here calling strindex()
    	if(strindex(line,pattern)>=0){
    		printf("%s",line);
    		found++;
    	}
    }
	return found;
}
//getline(): get line into s ,return length of line
//function defination means define task that function is going to perform
//we can use different names for arguement in declaration and defination of function
//but arguement should have same type and order
int getlines(char s[],int lim){
	int c,i=0;
	//getchar() (get character) takes character i.e input entered by user through terminal (linux) or turbo C (windows)
	//here is automatic conversion of charcter to its ascii value in order store it in integer type variable  
	//EOF stands for end of file
	while(--lim > 0 && (c = getchar())!= EOF && c!='\n'){
		s[i++]=c;
	}
	if(c == '\n'){
		s[i++] = c;
	}
	s[i] = '\0';
	//returning back from where it has been called
	return i;
}

//strindex(): return index of t in s, -1 if none
int strindex(char s[],char t[]){
	int i,j,k;
	for(i = 0;s[i]!='\0';i++){
		for(j=i,k=0; t[k]!='\0' && s[j]==t[k];j++,k++)
			;
        if(k>0 && t[k] == '\0'){
        	return i;
        }
	}
	return -1;
}
