import java.util.*;
class InertionSort{
	static void insertion_sort(int arr[],int n){
		int currEle,j;
		for(int i=1;i<n;i++){
			currEle=arr[i];
			j=i-1;
			while(j>=0&&arr[j]>currEle){
				arr[j+1]=arr[j];
				j--;
			}
			arr[j+1]=currEle;
		}
	}
	public static void main(String args[]){
		int arr[]=new int[]{5,6,1,8,3,9,4,0};
		int n=arr.length;
		insertion_sort(arr,n);
		System.out.println("Sorted array is ");
		for(int i=0;i<n;i++){
		    System.out.println(arr[i]);
	    }
	}
}