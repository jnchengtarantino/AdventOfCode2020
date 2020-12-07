import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day7 {
    public static void main(String[] args) {
        File file = new File("day7input.txt");
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(file));
            String text = null;
            DAG dag = new DAG();

            //part 1
            while ((text = reader.readLine()) != null) {
                String[] msg = text.strip().split(" ");
                String des = msg[0] + " " + msg[1];
                Node temp = dag.findByDescriptor(des);
                if(temp == null) {
                    temp = new Node(des);
                    dag.addNode(temp);
                }
                for (int i = 4; i < msg.length; i++){
                    if(msg[i].equals("bag,") || msg[i].equals("bags,") || msg[i].equals("bag.") || msg[i].equals("bags.")){
                        des = msg[i-2] + " " + msg[i-1];
                        if (des.equals("no other")) continue;
                        int amount = Integer.parseInt(msg[i-3]);
                        Node temp2 = dag.findByDescriptor(des);
                        if(temp2 == null) {
                            temp2 = new Node(des);
                            dag.addNode(temp2);
                        }
                        temp.addChild(temp2,amount);
                    }
                }     
            }

            System.out.println("Reached end of file");
            dag.buildDag();
            Node shinyGold = dag.findByDescriptor("shiny gold");
            System.out.println(dag.contains(shinyGold) - 1);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (reader != null) {
                    reader.close();
                }
            } catch (IOException e) {
            }
        }
    }

    private static class DAG{
        ArrayList<Node> nodes;
        ArrayList<Node> roots;

        DAG(){
            nodes = new ArrayList<Node>();
            roots = new ArrayList<Node>();
        }

        public void addNode(Node node){
            nodes.add(node);
        }

        public void buildDag(){
            for(Node node: nodes){
                for(Node child: node.children){
                    child.addParent(node);
                }
            }

            for(Node node: nodes){
                if (node.parents.size() == 0) roots.add(node);
            }
        }

        public LinkedHashSet<Node> getAncestors(Node node){
            if (node.parents.size() == 0){
                LinkedHashSet<Node> result = new LinkedHashSet<Node>();
                result.add(node);
                System.out.println(node.descriptor);
                return result;
            } else {
                LinkedHashSet<Node> result = new LinkedHashSet<Node>();
                for (Node parent : node.parents) result.addAll(getAncestors(parent));
                result.add(node);
                return result;
            }
        }

        public int contains(Node node){
            if(node.children.size() == 0) return 1;
            int result = 0;
            for(int i = 0; i < node.children.size(); i++){
                int temp = contains(node.children.get(i));
                result += (node.childrenAmount.get(i) * temp);
                System.out.println(node.descriptor + " contains " + node.childrenAmount.get(i) + " " + node.children.get(i).descriptor);
            }
            return result + 1;
        }

        public Node findByDescriptor(String des){
            for (Node node : nodes){
                if (des.equals(node.descriptor)) return node;
            }
            return null;
        }
    }

   private static class Node{
        ArrayList<Node> children;
        ArrayList<Integer> childrenAmount;
        ArrayList<Node> parents;
        String descriptor;

        Node(String descriptor){
            System.out.println("Creating node " + descriptor);
            this.descriptor = descriptor;
            children = new ArrayList<Node>();
            parents = new ArrayList<Node>();
            childrenAmount = new ArrayList<Integer>();
        }

        public void addChild(Node child, int amount){
            System.out.println("Adding " +  this.descriptor + " < * " + amount + " " + child.descriptor);
            children.add(child);
            childrenAmount.add(amount);
        }

        public void addParent(Node parent){
            parents.add(parent);
            // System.out.println("Adding " +  this.descriptor + " > " + parent.descriptor);
        }
   }
}
