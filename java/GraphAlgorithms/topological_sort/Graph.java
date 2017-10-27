package topological_sort;

import java.util.LinkedList;
import java.util.Stack;

/**
 * Created by USER on 27-10-2017.
 */
public class Graph {
    int vertex;
    LinkedList<Integer> adjlist[];
    Stack<Integer> finishing;
    private final boolean directed;
    Graph(int vertex,boolean directed){
        this.vertex=vertex;
        adjlist=new LinkedList[vertex];
        this.directed=directed;
        finishing=new Stack();
        for(int i=0;i<vertex;i++){
            adjlist[i]=new LinkedList<Integer>();
        }
    }

    void addEdges(int u,int v){
        adjlist[u].add(v);
        if(!directed){
            adjlist[v].add(u);
        }
    }

    void DFS(){
        int visited[]=new int[vertex];
        for(int i=0;i<vertex;i++){
            if(visited[i]==0){
                DFS_VISIT(i,visited);
            }
        }
        while(!finishing.isEmpty()){
            System.out.print(finishing.pop()+" ");
        }


    }

    void DFS_VISIT(int u,int []visited){
        visited[u]=1;
        for (Integer v:adjlist[u]){
            if (visited[v]==0){
                DFS_VISIT(v,visited);
            }
        }
        visited[u]=2;
        finishing.push(u);
    }

    void printEdges(){
        for(int i=0;i<vertex;i++){
            System.out.println("Adjacency List for vertex "+i);
            System.out.print("Head");
            for (Integer temp:adjlist[i]){
                System.out.print("--> "+temp);
            }
            System.out.println();
        }
    }
}