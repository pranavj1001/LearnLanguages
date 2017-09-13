import java.util.Arrays;
class MaxHeap{
	private int heap[];
	private int size;
	public MaxHeap(int a[]){
		size=a.length;
		heap=Arrays.copyOf(a,a.length);
	}

	public void build_maxheap(){
		for(int i=size/2-1;i>=0;i--){
			max_heapify(i);
		}
	}

	public void max_heapify(int i){
		int r=right(i);
		int l=left(i);
		int largest;
		if(l<size && heap[l]>heap[i]){
			largest=l;
		}
		else {
			largest=i;
		}
		if(r<size && heap[r]>heap[largest]){
			largest=r;
		}
		if(largest != i){
			exchange(i,largest);
			max_heapify(largest);
		}
	}

	private int right(int i){
		return 2*i+2;
	}

	private int left(int i){
		return 2*i+1;
	}

	private int parent(int i){
	    return (int)(i/2);
    }

    private void exchange(int i,int j){
    	int temp;
    	temp=heap[i];
    	heap[i]=heap[j];
    	heap[j]=temp;
    }

    public void print(){
    	for (int i = 0;i<size ;i++ ) {
    		System.out.println(heap[i]);
    	}
    }

    public int max_of_heap(){
    	return heap[0];
    }


}
class Heap{
	public static void main(String arg[]){
		int a[]=new int[]{4,1,3,2,16,9,10,14,8,7};
		MaxHeap max_heap=new MaxHeap(a);
		
        System.out.println("----- Initial Arrays -----");

		max_heap.print();


		max_heap.build_maxheap();

		System.out.println("----- Max-Heap -----");

		max_heap.print();

		System.out.println("Maximun of heap  "+max_heap.max_of_heap());
	}
}