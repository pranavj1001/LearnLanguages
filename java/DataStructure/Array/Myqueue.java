import java.util.NoSuchElementException;
class Queue{
	final int MAXSIZE=50;
	private int queue[];
	private int start;
	private int end;
	private int len;

	Queue(){
		queue=new int[MAXSIZE];
		start=-1;
		end=-1;
		len=0;
	}

	void push(int ele){
		//initial stage ,first element is push in queue
		if(start == -1 && end == -1){
			start++;
			end++;
			queue[end]=ele;
			len++;
		}
		//push element in queue if queue is empty
		else if(end >= 0 && end < MAXSIZE-1){
			end++;
			queue[end]=ele;
			len++;
		}
		else{
			System.out.println("Unable to push ,Queue is full");
		}
	}

	void pop(){
		//Queue is empty
		if(start==-1){
			System.out.println("Queue is Empty");
		}
		//check positon pointed by start
		else if(start>=0 && start<MAXSIZE){
			//start and end pointing to same position i.e queue is empty
			if(start==end){
				start=-1;
				end=-1;
				System.out.println("Queue is Empty");
			}
			//queue is not empty ,popping out element pointed by start
			else{
				int ele =queue[start];
				start++;
				System.out.println("Pop element "+ele);
				len--;
			}
		}
	}

	
	// return length of queue
	int lenQueue(){
		return len;
	}

	//display queue element
	void display(){
		if(len>0){
			System.out.println("------Queue------");
			for (int i=start;i<=end ;i++ ) {
				System.out.println(queue[i]);
			}
		}
		else {
			System.out.println("Queue is empty");
		}
	}

	//return  top element of queue
	int topQueue(){
		if(len>0){
           return queue[start];
		}
		else{
			throw new NoSuchElementException("Underflow Exception");
		}
	}


}
class Myqueue{
	public static void main(String[] args) {
		Queue myQueue1=new Queue();

		System.out.println("-----push element in queue-----");
		for (int i=0;i<10 ;i++ ) {
			System.out.println(i*2);
			myQueue1.push(i*2);
		}

		myQueue1.display();

		System.out.println("length of Queue "+myQueue1.lenQueue());
           
        System.out.println("-----pop element from queue-----");
		for (int i=0;i<5 ;i++ ) {
			myQueue1.pop();
		}

		myQueue1.display();
		System.out.println("length of Queue "+myQueue1.lenQueue());

        System.out.println("-----Top Element-----");
		try{
			System.out.println("Top Element of Queue "+myQueue1.topQueue());
		}
		catch (Exception e) {
			System.out.println("Error "+e.getMessage());
		}
	}
}