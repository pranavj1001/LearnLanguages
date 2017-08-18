/**
 * Created by Pranav Jain on 19-Aug-17.
 */

import java.util.ArrayList;
import java.util.List;

public class Vertex {

    //necessary variables
    private int data;
    private boolean visited;
    private List<Vertex> neighbourList;

    //constructor to get the things started
    public Vertex(int data){
        this.data = data;
        this.neighbourList = new ArrayList<>();
    }

    //method to add a neighbour
    public void addNeighbour(Vertex vertex){
        this.neighbourList.add(vertex);
    }

    //getter for data
    public int getData() {
        return data;
    }

    //setter for data
    public void setData(int data) {
        this.data = data;
    }

    //getter for visited
    public boolean isVisited() {
        return visited;
    }

    //setter for visited
    public void setVisited(boolean visited) {
        this.visited = visited;
    }

    //getter for neighbour list
    public List<Vertex> getNeighbourList() {
        return neighbourList;
    }

    @Override
    public String toString() {
        return "" + this.data;
    }
}
