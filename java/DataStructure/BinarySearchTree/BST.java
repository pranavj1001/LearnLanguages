package BinarySearchTree;
class BST{
	//this will be pointing to root of tree
	Node root;
	BST(){
		root=null;
	}
	void insert(int d){
		if(root==null){
			Node newNode = new Node (d) ;
			root=newNode;
		}
		else{
			inserting(root,d);
		}
		System.out.println("Successfully inserted  node "+d);
	}

	void inserting(Node tempRoot,int d){
		if(tempRoot.data > d){
		 	if(tempRoot.left == null){
		 		tempRoot.left=new Node(d);
		 	}
		 	else{
		 		inserting(tempRoot.left,d);
		 	}
		}
		else if (tempRoot.data == d) {
		 	//return 0;
		}
		else {
		 	if(tempRoot.right == null){
		 		tempRoot.right=new Node(d);
		 	}
		 	else{
		 		inserting(tempRoot.right,d);
		 	}
		}
	}
	void preorder(Node root){
		if(root == null){
			//System.out.println("tree is Empty");
		}
		else {
			System.out.print(root.data+" ");
			preorder(root.left);
			preorder(root.right);
		}
	}
	void inorder(Node root){
		if (root == null) {
			//System.out.println("tree is Empty");
		}
		else {
			inorder(root.left);
			System.out.print(root.data+" ");
			inorder(root.right);
		}
	}
	void postorder(Node root){
		if (root == null) {
			//System.out.println("tree is Empty");
		}
		if (root != null) {
			postorder(root.left);
			postorder(root.right);
			System.out.print(root.data+" ");
		}
	}
	void getMin(Node root){
		if(root.left == null){
			System.out.println("Minimum value of node in tree:"+root.data);
		}
		else {
			getMin(root.left);
		}
	}
	void getMax(Node root){
		if(root.right == null){
			System.out.println("Maximum value of node in tree:"+root.data);
		}
		else {
			getMax(root.right);
		}
	}

	public static void main(String[] args) {
		BST binaryST=new BST();

		System.out.println("inserting node in trees");

		binaryST.insert(14);
		binaryST.insert(15);
		binaryST.insert(4);
		binaryST.insert(9);
		binaryST.insert(7);
		binaryST.insert(18);
		binaryST.insert(3);
		binaryST.insert(5);
		binaryST.insert(16);
		binaryST.insert(4);
		binaryST.insert(20);
		binaryST.insert(17);
		binaryST.insert(9);
		binaryST.insert(14);
		binaryST.insert(5);

        System.out.println("preorder traversal is");
		binaryST.preorder(binaryST.root);
		System.out.println();

		System.out.println("inorder traversal is");
		binaryST.inorder(binaryST.root);
		System.out.println();

		System.out.println("postorder traversal is");
		binaryST.postorder(binaryST.root);
		System.out.println();

		binaryST.getMin(binaryST.root);

		binaryST.getMax(binaryST.root);
	}
}