/**
 * Created by Pranav Jain on 19-Aug-17.
 */

import java.util.LinkedList;
import java.util.Queue;

public class BFS {

    public void BFS(Vertex root){

        //Queue is the interface and it is initialized as a LinkedList
        Queue<Vertex> queue = new LinkedList<>();

        //set the root vertex as visited and add it in the queue
        root.setVisited(true);
        queue.add(root);

        //loop while queue is not Empty
        while(!queue.isEmpty()){

            //pop a vertex
            Vertex actualVertex = queue.remove();
            System.out.print(actualVertex + "->");

            //get the vertex's neighbour list
            for(Vertex v : actualVertex.getNeighbourList()){
                //if the neighbour is visited then ignore else set it visited and add it to the queue
                if(!v.isVisited()){
                    v.setVisited(true);
                    queue.add(v);
                }
            }

        }

    }

}
