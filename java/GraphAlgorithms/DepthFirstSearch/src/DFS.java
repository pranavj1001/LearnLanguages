import java.util.Stack;

/**
 * Created by Pranav Jain on 19-Aug-17.
 */
public class DFS {
    
    public void DFS(Vertex root){

        //Stack is the interface and it is initialized as a LinkedList
        Stack<Vertex> stack = new Stack<>();

        //set the root vertex as visited and add it in the stack
        root.setVisited(true);
        stack.push(root);

        //loop while stack is not Empty
        while(!stack.isEmpty()){

            //pop a vertex
            Vertex actualVertex = stack.pop();
            System.out.print(actualVertex + "->");

            //get the vertex's neighbour list
            for(Vertex v : actualVertex.getNeighbourList()){
                //if the neighbour is visited then ignore else set it visited and add it to the stack
                if(!v.isVisited()){
                    v.setVisited(true);
                    stack.push(v);
                }
            }

        }
        
    }
    
}
