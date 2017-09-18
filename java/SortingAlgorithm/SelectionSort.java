class SelectionSort{
	public static void selection_sort(int arr[],int n){
		int temp,pos;
		for(int i=0;i<n;i++){
			temp=arr[i];
		    pos=i;; 
			for(int j=i+1;j<n;j++){
				if(temp>arr[j]){
					temp=arr[j];
					pos=j;
				}
			}
			arr[pos]=arr[i];
			arr[i]=temp;
		}
	}
	public static void main(String[] args) {
		int arr[]=new int[]{5,3,4,9,1,0,7,2};
		selection_sort(arr,8);
		for (int i=0;i<8 ;i++ ) {
			System.out.println(arr[i]);																							
		}
	}
}