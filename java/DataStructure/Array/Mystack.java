class Stack{
	final int SIZE=50;
	private int stack[]=new int[SIZE];
	private int top;

	Stack(){
		top=0;
	}
	void push(int ele){
		stack[top]=ele;
		top++;
	}
	int pop(){
		if(top>0){
		    return stack[--top];
	    } 
	    else {
	    	return -1;
	    } 

	}
	void display(){
		System.out.println("Stack is (starting from top)");
		for(int i=top-1;i>=0;i--){
			System.out.print(stack[i]+" ");
		}
	}
	int tops(){
		return top;
	}
}

class Mystack{
	public static void main(String[] args) {
	Stack mystack1 = new Stack();

	for(int i=0;i<15;i++){
        mystack1.push(i*10);
	}

	mystack1.display();

	System.out.println();

	for(int i=0;i<5;i++){
        System.out.println("pop "+mystack1.pop());  
	}

	mystack1.display();

	System.out.println("\ntop : "+mystack1.tops());

	}
}