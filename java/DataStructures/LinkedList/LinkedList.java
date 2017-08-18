package LinkedList;
class LinkedList{
	int size;
	Node head;
    Node last;

	LinkedList(){
		size=0;
		head=null;
		last=null;
	}

	void insertAtEnd(int data){
		Node newNode=new Node(data);
		if(head==null){
			head=newNode;
			last=newNode;
		}
		else {
			last.next=newNode;
			last=newNode;
		}
		size++;
		System.out.println(data+" Sucessfully inserted");
	}

	void insertAtPos(int data,int pos){
		int tempPos=pos;
		Node temp;
		temp=head;
		if(size>=pos){
			if(pos==0){
				Node newNode=new Node(data);
				newNode.next=head;
				head=newNode;
				size++;
			}
			else if(size==pos){
				Node newNode=new Node(data);
				last.next=newNode;
				last=newNode;
				size++;
			}
			else{
				while(tempPos>1){
				    temp=temp.next;
					tempPos--;
				}
				Node temp1;
				Node newNode=new Node(data);
				temp1=temp.next;
				temp.next=newNode;
				newNode.next=temp1;
				size++;
		    }
			System.out.println(data+" Sucessfully inserted at "+pos);
		}
		else{
			System.out.println("Size of list is less than poition where you want to insert Node");
		}
	}

	void remove(){
		if(head==null){
			System.out.println("List is Empty");
		}
		else{
		    Node temp;
		    temp=head;
			int delPos=size-1;
			while(delPos>1){
				temp=temp.next;
			    delPos--;
			}
			System.out.println("removed node is "+(temp.next).data);
		    temp.next=null;
		    last=temp;
			size--;
		}
	}

	int lenOfList(){
		return size;
	}

	void traverse(){
		Node temp;
		temp=head;
		if(head!=null){
			System.out.println("----traversing list----");
			while(temp.next!=null){
				System.out.print(temp.data+" --> ");
				temp=temp.next;
			}
			System.out.println(temp.data);
	    }
	    else{
	    	System.out.println("List is Empty");
	    }

	}

	public static void main(String[] args) {
        LinkedList ll=new LinkedList();

        System.out.println("----inserting at end---- ");

        ll.insertAtEnd(55);
        ll.insertAtEnd(44);
        ll.insertAtEnd(23);
        ll.insertAtEnd(78);
        ll.insertAtEnd(12);
        ll.insertAtEnd(43);
        ll.insertAtEnd(92);
        ll.insertAtEnd(83);
        ll.insertAtEnd(61);
        ll.insertAtEnd(43);

        System.out.println("Length of List :"+ll.lenOfList());

		ll.traverse();

		ll.insertAtPos(100,4);

		System.out.println("Length of List :"+ll.lenOfList());

		ll.traverse();

		ll.insertAtPos(990,ll.lenOfList());

		System.out.println("Length of List :"+ll.lenOfList());

		ll.traverse();

		ll.insertAtPos(77,0);

		System.out.println("Length of List :"+ll.lenOfList());

		ll.traverse();

		ll.remove();

		System.out.println("Length of List :"+ll.lenOfList());

		ll.traverse();

    }

}