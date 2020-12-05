import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day2 {
    public static void main(String[] args) {
        int valid = 0;
        File file = new File("day2input.txt");
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(file));
            String text = null;

            //part 1
            // while ((text = reader.readLine()) != null) {
            //     String[] msg = text.split(" ",3);
            //     String[] bounds = msg[0].split("-");
            //     int min = Integer.parseInt(bounds[0]);
            //     int max = Integer.parseInt(bounds[1]);
            //     char match = msg[1].charAt(0);
            //     long count = msg[2].chars().filter(ch -> ch == match).count();

            //     if(count >= min && count <= max) valid++;
            // }

            //part 2
            while ((text = reader.readLine()) != null) {
                String[] msg = text.split(" ",3);
                String[] bounds = msg[0].split("-");
                int min = Integer.parseInt(bounds[0]);
                int max = Integer.parseInt(bounds[1]);
                char match = msg[1].charAt(0);
                try{
                    if((match == msg[2].charAt(min - 1)) ^ (match == msg[2].charAt(max - 1))) valid++;
                }
                catch(IndexOutOfBoundsException e){
                    System.out.println("error with string " + text);
                    System.out.println(e);
                }
            }
            System.out.println("valid: " + valid);
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
