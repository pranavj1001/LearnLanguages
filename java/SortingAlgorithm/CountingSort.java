class CountingSort{
	public static void counting_sort(int a[],int b[],int k){
		int c[]=new int[k];
		for (int j=0;j<a.length ;j++ ) {
			c[a[j]]=c[a[j]]+1;
		}
		for (int i=1;i<k ;i++ ) {
			c[i]=c[i]+c[i-1];
		}
		for(int i=0;i<a.length;i++){
			b[c[a[i]]-1]=a[i];
			c[a[i]]=c[a[i]]-1;
		}
	}
	public static void main(String[] args) {
		int a[]=new int[]{5,5,6,3,2,4,1,1,0,0,2,7};
		int b[]=new int [12];
		System.out.println("----------Before Sorting----------");
		for (int j=0;j<b.length ;j++ ) {
			System.out.print(a[j]+"  ");
		}
		counting_sort(a,b,8);
		System.out.println("\n----------After Sorting----------");
		for (int j=0;j<b.length ;j++ ) {
			System.out.print(b[j]+"  ");
		}
		System.out.println();
	}
}