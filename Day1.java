import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day1{
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>();
        File file = new File("day1input.txt");
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(file));
            String text = null;

            //part 1
            while ((text = reader.readLine()) != null) {
                int num = Integer.parseInt(text);
                for (int i = 0; i < list.size(); i++){
                    if((list.get(i) + num) == 2020){
                         System.out.println(list.get(i) + " * " + num + " = " + list.get(i)*num);
                    }
                }
                list.add(num);
            }

            //part 2
            for (int i = 0; i < list.size(); i++){
                for (int j = 0; j < list.size(); j++){
                    for (int k = 0; k < list.size(); k++){
                        if (2020 == (list.get(i) + list.get(j) + list.get(k))){
                            System.out.println(list.get(i)+" * "+list.get(j)+" * "+list.get(k)+" = "+list.get(i)*list.get(j)*list.get(k));
                            return;
                        }
                    }
                }
            }
            System.out.println("Reached end of file");
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
}