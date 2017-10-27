package topological_sort;

/**
 * Created by USER on 27-10-2017.
 */
public class Main {
    public static void main(String ags[]){
        Graph gp =new Graph(6,true);
        gp.addEdges(5,2);
        gp.addEdges(5,0);
        gp.addEdges(4,0);
        gp.addEdges(4,1);
        gp.addEdges(2,3);
        gp.addEdges(3,1);

        //gp.printEdges();
        gp.DFS();
    }
}
